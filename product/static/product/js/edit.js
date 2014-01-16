(function($, global) {

    function toggelFormErrors(toggle) {
        $('#formErrors').toggle(toggle);
    }

    function onEditProductSubmit(form) {
        toggelFormErrors(false);

        var form = $(this),
            productName = $('#name', form).val(),
            productCarbohydrates = $('#carbohydrates', form).val(),
            glycemicIndex = $('#glycemic_index', form).val(),
            submitData = {
                'name': productName,
                'carbohydrates': productCarbohydrates,
                'glycemic_index': glycemicIndex
            };

        function onCreateSuccess(data) {
            global.location.href = global.Diabetto.urlProductDetails;
        }

        function onCreateError(data) {
            toggelFormErrors(true);
        }

        $.ajax({
            'url': global.Diabetto.urlUpdateProduct,
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
        $('#formEditProduct').submit(onEditProductSubmit);

        $("#popupEditProduct").on("popupafterclose", function(event, ui) {
            toggelFormErrors(false);
        });
    });

})(jQuery, window);