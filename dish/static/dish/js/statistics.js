(function($, _, global) {
    var selectorProductWeightInput = '.product-weight-field input',
        selectorStatisticsWeight = '#statistics-weight',
        selectorCarbohydrateUnits = '#statistics-carbohydrate-units',
        selectorProductLi = 'li[data-product-id]',
        selectorProductsList = '#products-list',
        selectorCarbohydrateUnitsPerPortion = '#statistics-carbohydrate-units-in-portion',
        selectorPortonsInput = '#id_portions';


    global.Diabetto = global.Diabetto || {};
    global.Diabetto.Statistics = {
        updateStatistics: function() {
            Statistics = global.Diabetto.Statistics;

            Statistics.updateStatisticsWeight();
            Statistics.updateStatisticsCarbohydrateUnits();
            Statistics.updateStatisticsCarbohydratePerPortion();
        },

        updateStatisticsWeight: function() {
            $(selectorStatisticsWeight).html(getProductsWeight() + ' г.');
        },

        updateStatisticsCarbohydrateUnits: function() {
            $(selectorCarbohydrateUnits).html(getCarbohydrateUnits().toFixed(2));
        },

        updateStatisticsCarbohydratePerPortion: function() {
            $(selectorCarbohydrateUnitsPerPortion).html(
                getCarbohydrateUnitsPerPortion().toFixed(2));
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
        /* Calculate all added products carbohydrates units */

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


    function getCarbohydrateUnitsPerPortion() {
        /* Calculate all added products carbohydrate units per portion */

        var carbohydrateUnits = getCarbohydrateUnits(),
            portions = parseInt($(selectorPortonsInput).val());

        return carbohydrateUnits / portions;
    }

})(jQuery, _, window);