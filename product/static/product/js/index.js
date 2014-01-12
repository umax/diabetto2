(function($, global) {

    function onNewProductSubmit(form) {
        $('#formErrors').hide();

        var productName = $('#name').val(),
            submitData = {
                'name': productName
            };

        function onCreateSuccess() {
            global.location.href = global.Diabetto.urlProducts;
        }

        function onCreateError(data) {
            $('#formErrors').show();
        }
        
        $.ajax({
            'url': global.Diabetto.urlCreateProduct,
            'async': false,
            'type': 'POST',
            'data': submitData,
            'dataType': 'json',
            'success': onCreateSuccess,
            'error': onCreateError
        });

        return false;
    }

    $(document).ready(function() {
        $('#formNewProduct').submit(onNewProductSubmit);

        $("#popupNewProduct").on("popupafterclose", function(event, ui) {
            $('#formErrors').hide();
        });
    });

})(jQuery, window);