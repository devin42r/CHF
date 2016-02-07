/**
 * Created by devin on 2/3/16.
 */

$(function() {

    console.log($('#loginform'))

        // bind form using ajaxForm
        $('#loginform').ajaxForm({
            // target identifies the element(s) to update with the server response
            target: '#jquery-loadmodal-js-body',
        });

}); //ready