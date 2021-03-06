(function($, _, global) {
    var selectorFilterMenu = '#filter-menu',
        selectorButtonAddProduct = '.js-button-add-product',
        selectorButtonRemoveProduct = '.remove-product-button',

        selectorFilterMenu = '#filter-menu',
        selectorProductsList = '#products-list',
        selectorPortionsInput = '#id_portions',
        selectorProductWeightInput = '.product-weight-field input',
        selectorDishComments = '.dish-comments',

        selectorButtonPortionsMinus = '.button-portion-minus',
        selectorButtonPortionsPlus = '.button-portion-plus',

        selectorButtonScrollUp = '.scroll-up-button',
        selectorButtonScrollDown = '.scroll-down-button',

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

    function onButtonPortionsMinusClick(event) {
        event.preventDefault();

        var portions = parseInt($(selectorPortionsInput).val());
        if (portions) {
            portions -= 1;
            if (portions <= 0) {
                portions = 1;
            }
            $(selectorPortionsInput).val(portions);
            global.Diabetto.Statistics.updateStatistics();
        }

    }

    function onButtonPortionsPlusClick(event) {
        event.preventDefault();

        var portions = parseInt($(selectorPortionsInput).val());
        if (portions) {
            portions += 1;
            $(selectorPortionsInput).val(portions);
            global.Diabetto.Statistics.updateStatistics();
        }
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

    function onScrollUpButtonClick(event) {
        var commentsEl = $(selectorDishComments);
        commentsEl.animate({
            'scrollTop': commentsEl.scrollTop() - 100
        }, 100);
    }

    function onScrollDownButtonClick(event) {
        var commentsEl = $(selectorDishComments);
        commentsEl.animate({
            'scrollTop': commentsEl.scrollTop() + 100
        }, 100);
    }


    $(document).ready(function() {
        $(selectorFilterMenu).change(onFilterMenuChange);
        $(selectorButtonAddProduct).click(onAddProductButtonClick);
        $(selectorButtonPortionsPlus).click(onButtonPortionsPlusClick);
        $(selectorButtonPortionsMinus).click(onButtonPortionsMinusClick);
        $(selectorButtonScrollUp).click(onScrollUpButtonClick);
        $(selectorButtonScrollDown).click(onScrollDownButtonClick);
        $(document).on('click', selectorButtonRemoveProduct,
                       onRemoveProductButtonClick);
        $(document).on('input', selectorProductWeightInput,
                       global.Diabetto.Statistics.updateStatistics);
        $(document).on('input', selectorPortionsInput,
                       global.Diabetto.Statistics.updateStatistics);

        productsList = $(selectorProductsList);
        productTemplate = _.template($('#product-template').text());
        global.Diabetto.Statistics.updateStatistics();
    });

})(jQuery, _, window);
