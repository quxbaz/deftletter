$(function() {
    var $table = $('#customize table');
    var $tr = $('tr:not(.header-row)', $table);
    $table.on('click', 'td', function() {
        var $picked = $(this).closest('tr');
        $tr.not($picked).removeClass('picked');
        $picked.toggleClass('picked');
    });
});