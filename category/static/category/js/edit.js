(function($, global) {

    function toggleFormErrors(toggle) {
        $('#formErrors').toggle(toggle);
    }

    function onEditCategorySubmit(form) {
        toggleFormErrors(false);

        var form = $(this),
            categoryName = $('#name', form).val(),
            submitData = {
                'name': categoryName
            };

        function onCreateSuccess() {
            global.location.href = global.Diabetto.urlCategoryDetails;
        }

        function onCreateError(data) {
            toggleFormErrors(true);
        }
        
        $.ajax({
            'url': global.Diabetto.urlUpdateCategory,
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
        $('#formEditCategory').submit(onEditCategorySubmit);

        $("#popupEditCategory").on("popupafterclose", function(event, ui) {
            toggleFormErrors(false);
        });
    });

})(jQuery, window);