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


define([
    'base/js/namespace',
    'base/js/promises'
], function (Jupyter, promises) {
    promises.app_initialized.then(function (appname) {
        if (appname === 'NotebookApp') {
            console.log('woooo');

            Jupyter.notebook.set_autosave_interval(0);
            $('#maintoolbar-container').append(`            <a href="#" onclick="Jupyter.notebook.execute_all_cells();" class="btn btn-success">Run all</a>
            <a href="#" onclick="Jupyter.notebook.clear_all_output();" class="btn btn-success">Clear output</a>`);


            $('#notebook').append(`
            <div style="z-index: 1000000; top: 130px; bottom: 0; right: 20px; position: fixed; width: 300px;">

            
            <p>Activities</p>
            <div class="row">
            <div class="col">
            <input type="text" placeholder="Search" class="form-control" id="search_activities" onBlur="Jupyter.keyboard_manager.enable();" onFocus="Jupyter.keyboard_manager.disable();">
            </div>
            <div>
    <div class="panel-group" role="tablist">
        <div class="panel panel-default">
            <div class="panel-heading" role="tab" id="excel">
                <h4 class="panel-title">
                    <a class="collapsed" data-toggle="collapse" href="#gr1" aria-expanded="false" aria-controls="gr1">
                        Excel
                    </a>
                </h4>
            </div>
            <div id="gr1" class="panel-collapse collapse" role="tabpanel" aria-labelledby="excel">
                <ul class="list-group">
                    <li class="list-group-item"><a href="#" class="btn"
                            onClick="insertSnippet('code', 'hello world');">Insert code</a></li>
                    <li class="list-group-item"><a href="#" class="btn"
                            onClick="insertSnippet('code', 'hello world');">Insert code</a></li>
                    <li class="list-group-item"><a href="#" class="btn"
                            onClick="insertSnippet('code', 'hello world');">Insert code</a></li>
                </ul>
            </div>
            <div class="panel-heading" role="tab" id="word">
                <h4 class="panel-title">
                    <a class="collapsed" data-toggle="collapse" href="#gr2" aria-expanded="false" aria-controls="ge2">
                        Word
                    </a>
                </h4>
            </div>
            <div id="gr2" class="panel-collapse collapse" role="tabpanel" aria-labelledby="word">
                <ul class="list-group">
                    <li class="list-group-item"><a href="#" class="btn"
                            onClick="insertSnippet('code', 'hello world');">Insert code</a></li>
                    <li class="list-group-item"><a href="#" class="btn"
                            onClick="insertSnippet('code', 'hello world');">Insert code</a></li>
                    <li class="list-group-item"><a href="#" class="btn"
                            onClick="insertSnippet('code', 'hello world');">Insert code</a></li>
                </ul>
            </div>
        </div>
    </div>
    
</div>
            `);



        }
    });
});

function insertSnippet(cell_type, contents) {
    cell = Jupyter.notebook.insert_cell_below(cell_type);
    cell.set_text(contents)
}


