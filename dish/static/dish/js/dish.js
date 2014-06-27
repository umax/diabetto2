(function($, _, global) {
    var selectorFilterMenu = '#filter-menu',
        selectorButtonAddProduct = '.js-button-add-product',
        selectorButtonRemoveProduct = '.remove-product-button',

        selectorFilterMenu = '#filter-menu',
        selectorProductsList = '#products-list',
        selectorPotionsInput = '#id_portions',
        selectorProductWeightInput = '.product-weight-field input',

        productTemplate = null,
        productsList = null;


    function onAddProductButtonClick(event) {
        $(selectorFilterMenu).selectmenu("open");
    }


    function onRemoveProductButtonClick(event) {
        $(this).closest('li').remove();
        productsList.listview('refresh');
        global.Diabetto.Statistics.updateStatistics();
    }


    function onFilterMenuChange(event) {
        /* Add selected product to products list */

        var productId = $(this).val(),
            productCarbohydrates = $(this).data('data-product-carbohydrates'),
            productAlreadyAdded = $('li[data-product-id=' + productId + ']').length;

        if (productAlreadyAdded) {
            return;
        }

        var productName = $(this).find("option:selected").text(),
            productEl = $(productTemplate({
                'productId': productId,
                'productName': productName,
                'productWeight': 0,
                'productCarbohydrates': productCarbohydrates
            }));

        productsList.append(productEl).listview('refresh');
        global.Diabetto.Statistics.updateStatistics();
    }


    $(document).ready(function() {
        $(selectorFilterMenu).change(onFilterMenuChange);
        $(selectorButtonAddProduct).click(onAddProductButtonClick);
        $(document).on('click', selectorButtonRemoveProduct,
                       onRemoveProductButtonClick);
        $(document).on('input', selectorProductWeightInput,
                       global.Diabetto.Statistics.updateStatistics);
        $(selectorPotionsInput).change(global.
            Diabetto.Statistics.updateStatisticsCarbohydratePerPortion);

        productsList = $(selectorProductsList);
        productTemplate = _.template($('#product-template').text());
    });

})(jQuery, _, window);