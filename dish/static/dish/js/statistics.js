(function($, _, global) {
    var selectorProductWeightInput = '.product-weight-field input',
        selectorStatisticsWeight = '#statistics-weight',
        selectorCarbohydrateUnits = '#statistics-carbohydrate-units',
        selectorProductLi = 'li[data-product-id]',
        selectorProductsList = '#products-list';


    global.Diabetto = global.Diabetto || {};
    global.Diabetto.Statistics = {
        updateStatistics: function() {
            updateStatisticsWeight();
            updateStatisticsCarbohydrateUnits();
        }
    };


    function getProductsWeight() {
        /* Calculate all added products weight */

        var weight = 0, productWeight;

        _.each($(selectorProductWeightInput, $(selectorProductsList)), function(inputEl) {
            productWeight = parseInt(inputEl.value);
            if (productWeight) {
                weight += productWeight;
            }
        });

        return weight;
    }

    function getCarbohydrateUnits() {
        /* Calculate all added products carbohydrates */

        var carbohydrateUnits = 0.0,
            productId,
            productWeight,
            productCarbohydrates;

        _.each($(selectorProductLi), function(productLiEl) {
            productId = productLiEl.getAttribute('data-product-id');
            productWeight = parseInt(productLiEl.querySelector('input').value);
            productCarbohydrates = global.Diabetto.allProducts[productId].carbohydrates;

            carbohydrateUnits += (productCarbohydrates / 100.0 * productWeight / 12)
        });

        return carbohydrateUnits;
    }


    function updateStatisticsWeight() {
        $(selectorStatisticsWeight).html(getProductsWeight() + ' г.');
    }

    function updateStatisticsCarbohydrateUnits() {
        $(selectorCarbohydrateUnits).html(getCarbohydrateUnits().toFixed(2));
    }

})(jQuery, _, window);