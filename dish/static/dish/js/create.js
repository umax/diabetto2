(function($) {
    var selectorButtonAddProduct = '.js-button-add-product',
        selectorFilterMenu = '#filter-menu';


    $(document).ready(function() {
        $(selectorButtonAddProduct).click(function() {
            $(selectorFilterMenu).selectmenu("open");
        });
    });

})(jQuery);