function filename(path) {
    return path.replace(/^.*[\\\/]/, '');
}

$(function() {

    // Triggers a click on a proxy button's target when the proxy
    // button is clicked.
    $('.proxy-btn').click(function(e) {
        $('#' + $(this).attr('data-target')).click();
    });

    $('.submit-btn').click(function(e) {
        if ($('#file-btn').attr('value') != '')
            $(this).closest('form').submit();
        e.preventDefault();
    });

    $('#file-btn').change(function(e) {
        var max_chars = 48;
        var text = filename(this.value).substr(0, max_chars);
        if (text == '')
            text = "Click here to browse for an image";
        $('#image-path').text(text);
        // $('.submit-btn').click();  // Automatically upload the image.
    });

})
