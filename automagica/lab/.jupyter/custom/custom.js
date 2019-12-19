

requirejs([
    'jquery',
    'base/js/utils',
], function ($, utils
) {

    utils.change_favicon("custom/favicon.png")
});

$([Jupyter.events]).on("notebook_loaded.Notebook", function () {
    Jupyter.notebook.set_autosave_interval(0);

});

var htmlToInsert = '';

define([
    'base/js/namespace',
    'base/js/promises'
], function (Jupyter, promises) {
    promises.app_initialized.then(function (appname) {
        if (appname === 'NotebookApp') {
            Jupyter.notebook.set_autosave_interval(0);

            Jupyter.notebook.kernel.execute('from automagica.activities import *');


            $('#maintoolbar-container').append(`
            <a href="#" onclick="Jupyter.notebook.execute_all_cells();" class="btn btn-success">Run all</a>
            <a href="#" onclick="Jupyter.notebook.clear_all_output();" class="btn btn-success">Clear output</a>`);

            $('head').append('<link rel="stylesheet" href="https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css">')

            var categories;

            $.getJSON('https://raw.githubusercontent.com/OakwoodAI/Automagica/v2.0/docs/portal/activities.json', function (data) {
                categories = data;

                htmlToInsert += `
            <div style="z-index: 1000000; top: 150px; bottom: 0; left: 20px; position: fixed; width: 300px; overflow-y: scroll; height:800px;">
            <div class="panel-group" role="tablist">
            <div class="panel panel-default">`;
                categories.forEach(function (category, i) {

                    var category_keywords = '';

                    category.activities.forEach(function (activity) {
                        category_keywords += activity.keywords;
                    }
                    );

                    htmlToInsert += `
                <div data-keywords="`+ category_keywords + `" class="panel-heading category_container" role="tab" id="category_` + i + `">
                    <h4 class="panel-title">
                        <a class="collapsed" data-toggle="collapse" href="#`+ i + `" aria-expanded="false" aria-controls="` + i + `">
                            <i class="`+ category.icon + ` la-lw"></i>&nbsp;&nbsp;` + category.name + `
                        </a>
                    </h4>
                </div>
                <div id="`+ i + `" class="panel-collapse collapse category_panel" role="tabpanel" aria-labelledby="category_` + i + `">
                    <ul class="list-group">`;

                    category.activities.forEach(function (activity) {

                        htmlToInsert += `
                        <li data-keywords="`+ activity.keywords + `" class="list-group-item activity_container"><a data-title=` + JSON.stringify(activity.name) + ` data-snippet=` + JSON.stringify(activity.snippet) + ` href="#"
                                onClick="insertSnippet('markdown', '### ' + this.getAttribute('data-title')); insertSnippet('code', this.getAttribute('data-snippet')); " title="`+ activity.description + `"><i class="` + activity.icon + ` la-lw"></i>&nbsp;&nbsp;` + activity.name + `</a></li> `;

                    });

                    htmlToInsert += `
                    </ul>
                </div>`;
                });

                htmlToInsert += `</div></div></div>`;

                htmlToInsert += `
                <style>
                .displayNone {
                    display: none;
                }
            </style>
                `;

                var notebook = document.getElementById('notebook');
                notebook.insertAdjacentHTML('beforeend', htmlToInsert);





            })
        }
    });
});

function insertSnippet(cell_type, contents) {
    cell = Jupyter.notebook.insert_cell_below(cell_type);
    cell.set_text(contents.replace(/\\n/g, '\n'));
    if (cell_type == 'markdown') {
        cell.execute();

    }
    cell.focus_cell();
}

