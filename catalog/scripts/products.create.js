/**
 * Created by devin on 2/18/16.
 */
$('tr:has(input.hideThis)').hide()

$(function() {

        $('#id_product_type').on('change', function() {
          if ( this.value == 'BP') {
              $('tr:has(.hideThis)').hide()
              $('tr:has(input#quantity)').show()
          }
          else if ( this.value == 'IP') {
              $('tr:has(.hideThis)').hide()
              $('tr:has(#creator)').show()
          }
          else {
              $('tr:has(.hideThis)').hide()
              $('tr:has(select#status)').show()
              $('tr:has(input#purchase)').show()
          }
        }).trigger("change");
});