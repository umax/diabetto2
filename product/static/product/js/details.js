(function($, global) {

    $(document).ready(function() {
        $('#buttonDeleteProduct').click(function() {
            $.ajax({
  type: "POST",
  url: $(this).attr('href'),
  success: function() {global.location.href='/'},
});
        });
    });

})(jQuery, window);