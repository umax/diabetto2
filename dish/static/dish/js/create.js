(function($, _) {
    var selectorButtonAddProduct = '.js-button-add-product',
        selectorButtonRemoveProduct = '.remove-product-button',
        selectorFilterMenu = '#filter-menu',
        selectorProductsList = '#products-list',

        productTemplate = null,
        productsList = null;


    function onFilterMenuChange(event) {
        /* Add selected product to products list */

        var productId = $(this).val(),
            productName = $(this).find("option:selected").text(),
            productEl = $(productTemplate({
                'productId': productId,
                'productName': productName,
                'productWeight': 0
            }));

        productsList.append(productEl).listview('refresh');
    }


    function onAddProductButtonClick(event) {
        $(selectorFilterMenu).selectmenu("open");
    }


    function onRemoveProductButtonClick(event) {
        $(this).closest('li').remove();
        productsList.listview('refresh');
    }


    $(document).ready(function() {
        $(selectorButtonAddProduct).click(onAddProductButtonClick);
        $(selectorFilterMenu).change(onFilterMenuChange);
        $(document).on('click', selectorButtonRemoveProduct,
                       onRemoveProductButtonClick);

        productsList = $(selectorProductsList);
        productTemplate = _.template($('#product-template').text());
    });

})(jQuery, _);