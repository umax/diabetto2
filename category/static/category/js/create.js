(function($, global) {

    function toggleFormErrors(toggle) {
        $('#formErrors').toggle(toggle);
    }

    function onCreateCategorySubmit(form) {
        toggleFormErrors(false);

        var form = $(this),
            categoryName = $('#name', form).val(),
            submitData = {
                'name': categoryName
            };

        function onCreateSuccess() {
            global.location.href = global.Diabetto.urlCategories;
        }

        function onCreateError(data) {
            toggleFormErrors(true);
        }
        
        $.ajax({
            'url': global.Diabetto.urlCreateCategory,
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
        $('#formNewCategory').submit(onCreateCategorySubmit);

        $("#popupNewCategory").on("popupafterclose", function(event, ui) {
            toggleFormErrors(false);
        });
    });

})(jQuery, window);