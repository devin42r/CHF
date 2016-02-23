/**
 * Created by devin on 2/20/16.
 */
$('tr:has(input.hideThis)').hide()

$(function() {
    if ($('#product_type').text() == 'bulk product') {
        $('tr:has(.hideThis)').hide()
        $('tr:has(input#quantity)').show()
        $('h4').text('Bulk Product')
    }
    else if ($('#product_type').text() == 'individual product') {
        $('tr:has(.hideThis)').hide()
        $('tr:has(input#creator)').show()
        $('h4').text('Individual Product')
    }
    else {
        $('tr:has(.hideThis)').hide()
        $('tr:has(select#status)').show()
        $('tr:has(input#purchase)').show()
        $('h4').text('Rental Product')
    }
});

