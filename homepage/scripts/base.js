/**
 * Created by devin on 2/2/16.
 */

console.log($('#loginbutton'))

$(function() {

    $('#loginbutton').click(function () {

        $.loadmodal({
            url: '/account/login/',
            id: 'loginmodal',
            title: 'Login',

        })
    })
})