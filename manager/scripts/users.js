/**
 * Created by devin on 2/16/16.
 */

$(function() {

    $( ".delete" ).click(function(event) {

        event.preventDefault();
        var href = $(this).attr('href');
        $('#confirm_delete_button').attr('href', href);

        $('#delete_modal').modal('show');

    });

});