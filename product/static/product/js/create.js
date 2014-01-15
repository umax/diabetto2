(function($, global) {

    function toggleFormErrors(toggle) {
        $('#formErrors').toggle(toggle);
    }

    function onNewProductSubmit(form) {
        toggleFormErrors(false);

        var form = $(this),
            productName = $('#name', form).val(),
            productCarbohydrates = $('#carbohydrates', form).val(),
            submitData = {
                'name': productName,
                'carbohydrates': productCarbohydrates,
                'category': global.Diabetto.currentCategory
            };

        function onCreateSuccess(data) {
            global.location.href = global.Diabetto.urlCategoryDetails;
        }

        function onCreateError(data) {
            toggleFormErrors(true);
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
            toggleFormErrors(false);
        });
    });

})(jQuery, window);