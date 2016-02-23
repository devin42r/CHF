/**
 * Created by devin on 2/20/16.
 */


$(function() {

    $( ".delete" ).click(function(event) {

        event.preventDefault();
        var href = $(this).attr('href');
        $('#confirm_delete_button').attr('href', href);

        $('#delete_modal').modal('show');

    });

    //put the .load in here. The button for the load is located in the products.html
    //This JavaScript fuction will grab quantity data from the database and update it on the website.
    $( ".RefreshButton" ).click(function() {
    console.log("hello tyler")
    $(this).siblings('.quantityText').load( "/catalog/products.getquantity/" + $(this).attr('data-pid') );

 });

});

