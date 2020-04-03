

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


            $('a:contains("Kernel")').text('Bot');

            $('a:contains("Widgets")').hide();

            $('#cell_type option[value="raw"]').hide();
            $('#cell_type option[value="heading"]').hide();



            $('#maintoolbar-container').append(`
            <a href="#" onclick="Jupyter.notebook.execute_all_cells();" class="btn">Run all</a>
            <a href="#" onclick="Jupyter.notebook.clear_all_output();" class="btn">Clear output</a>`);

            $('head').append('<link rel="stylesheet" href="https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css">')

            var categories;

            $.getJSON('https://raw.githubusercontent.com/OakwoodAI/Automagica/master/docs/portal/activities.json', function (data) {
                categories = data;

                htmlToInsert += `
            <div id="activities" style="z-index: 1000000; top: 150px; left: 20px; position: fixed; width: 300px; background-color: white;" class="shadow">
            <div id="activitiesheader" style="cursor: move; font-size: 15px; padding: 10px; background-color: white;"><i class="las la-grip-vertical"></i> Activities</div>
            <div>
            <input type="text" placeholder="Search" class="form-control" id="search_activities" onkeyup="filterActivities(this.value);" onBlur="Jupyter.keyboard_manager.enable();" onFocus="Jupyter.keyboard_manager.disable();">
            </div>
            <div style=" overflow-y: scroll; height:600px;">
            <div class="panel-group" role="tablist">
            <div class="panel panel-default">`;
                categories.forEach(function (category, i) {

                    var category_keywords = '';

                    category.activities.forEach(function (activity) {
                        category_keywords += activity.keywords;
                    }
                    );

                    htmlToInsert += `
                <div data-keywords="`+ category_keywords + `" class="panel-heading category_header" id="category_header_` + i + `">
                    <h4 class="panel-title">
                        <a data-toggle="collapse" href="#" data-target="#category_` + i + `">
                            <i class="`+ category.icon + ` la-lw"></i>&nbsp;&nbsp;` + category.name + `
                        </a>
                    </h4>
                </div>

                <div data-keywords="`+ category_keywords + `" id="category_` + i + `" class="panel-collapse collapse category_panel">
                    <ul class="list-group">`;

                    category.activities.forEach(function (activity) {

                        htmlToInsert += `
                        <li data-keywords="`+ activity.keywords + `" class="list-group-item activity_container"><a data-title=` + JSON.stringify(activity.name) + ` data-snippet=` + JSON.stringify(activity.function_call) + ` href="#"
                                onClick="insertSnippet('code', this.getAttribute('data-snippet')); " title="`+ activity.description + `"><i class="` + activity.icon + ` la-lw"></i>&nbsp;&nbsp;` + activity.name + `</a></li> `;

                    });

                    htmlToInsert += `
                    </ul>
                </div>`;
                });

                htmlToInsert += `</div></div></div></div>`;

                htmlToInsert += `
                <style>
                .displayNone {
                    display: none;
                }
            </style>
                `;

                var notebook = document.getElementById('notebook');
                notebook.insertAdjacentHTML('beforeend', htmlToInsert);


                var buttonHTMLInsert = `
                <div id="recorder" class="btn-group">
                    <a href="#" title="Launch the Automagica Recorder" onclick="Jupyter.notebook.kernel.execute('from automagica import *; recorder()');" class="btn btn-default">🔴 Recorder (beta)</a>
                </div>
                `;

                var toolbar = document.getElementById('maintoolbar-container');
                toolbar.insertAdjacentHTML('beforeend', buttonHTMLInsert)

                dragElement(document.getElementById("activities"));



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

function filterActivities(q) {
    var category_panels = $('.category_panel');
    var category_headers = $('.category_header');
    var activity_containers = $('.activity_container')

    if (q.length > 0) {
        // hide panels and expand resulting panels
        category_panels.each(function (index) {
            if ($(this).attr('data-keywords').toLowerCase().includes(q.toLowerCase())) {
                $(this).collapse('show');
            }
        });

        // hide category buttons and show matches
        category_headers.each(function (index) {
            $(this).hide();
            if ($(this).attr('data-keywords').toLowerCase().includes(q.toLowerCase())) {
                $(this).show();
            }
        });

        // hide activiy buttons and show matches
        activity_containers.each(function (index) {
            $(this).hide();
            if ($(this).attr('data-keywords').toLowerCase().includes(q.toLowerCase())) {
                $(this).show();
            }
        });


    } else {
        category_panels.each(function (index) {
            //$(this).show();
            // $(this).collapse('show');
            $(this).collapse('hide');

        });

        category_headers.each(function (index) {
            $(this).show();
        });

        activity_containers.each(function (index) {
            $(this).show();
        });

    }
}


function dragElement(elmnt) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    if (document.getElementById(elmnt.id + "header")) {
        // if present, the header is where you move the DIV from:
        document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
    } else {
        // otherwise, move the DIV from anywhere inside the DIV:
        elmnt.onmousedown = dragMouseDown;
    }

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        // set the element's new position:
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }

    function closeDragElement() {
        // stop moving when mouse button is released:
        document.onmouseup = null;
        document.onmousemove = null;
    }
}