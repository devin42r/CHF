/**
 * Created by devin on 2/15/16.
 */


$(function () {
    $('#datetimepicker').datetimepicker({
        format: "YYYY-MM-DD"
    });
});

$(function () {
    $('#datetimepicker2').datetimepicker({
        format: "YYYY-MM-DD"
    });
});

$(function() {

    $( ".delete" ).click(function(event) {

        event.preventDefault();
        var href = $(this).attr('href');
        $('#confirm_delete_button').attr('href', href);

        $('#delete_modal').modal('show');

    });

});