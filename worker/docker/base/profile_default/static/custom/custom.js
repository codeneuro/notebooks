// single-window mode, sets all UI links to open in the same window
// doesn't affect links in notebook output
IPython._target = '_self';

require(["base/js/events"], function (events) {
    events.on("notebook_loaded.Notebook", function () {
        // disable warn-on-unsaved changes as these are ephemeral notebooks
        window.onbeforeunload = null;
        // additional custom js to force external links to stay in same window
        $('a').attr('target','_self')
    });
});
