(function($, _, global) {
    var selectorStatisticsWeight = '#statistics-weight',
        selectorStatisticsWeightPerPortion = '#statistics-weight-per-portion',
        selectorStatisticsCarbohydrateUnits = '#statistics-carbohydrate-units',
        selectorStatisticsCarbohydrateUnitsPerPortion = '#statistics-carbohydrate-units-per-portion',

        selectorProductLi = 'li[data-product-id]',
        selectorProductsList = '#products-list',
        selectorPortonsInput = '#id_portions';
        selectorProductWeightInput = '.product-weight-field input',


    global.Diabetto = global.Diabetto || {};
    global.Diabetto.Statistics = {
        updateStatistics: function() {
            Statistics = global.Diabetto.Statistics;

            Statistics.updateStatisticsWeight();
            Statistics.updateStatisticsCarbohydrateUnits();
            Statistics.updateStatisticsCarbohydratePerPortion();
            Statistics.updateStatisticsWeightPerPortion();
        },

        updateStatisticsWeight: function() {
            $(selectorStatisticsWeight).html(getProductsWeight() + ' г.');
        },

        updateStatisticsCarbohydrateUnits: function() {
            $(selectorStatisticsCarbohydrateUnits).html(getCarbohydrateUnits().toFixed(2));
        },

        updateStatisticsCarbohydratePerPortion: function() {
            $(selectorStatisticsCarbohydrateUnitsPerPortion).html(
                getCarbohydrateUnitsPerPortion().toFixed(2));
        },

        updateStatisticsWeightPerPortion: function() {
            $(selectorStatisticsWeightPerPortion).html(
                getProductsWeightPerPortion().toFixed(0) + ' г.');
        }
    };


    function getPortions() {
        /* Get current number of portions */

        return parseInt($(selectorPortonsInput).val());
    }


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


    function getProductsWeightPerPortion() {
        /* Calculate all added products weight per portion */

        return getProductsWeight() / getPortions();
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

        return getCarbohydrateUnits() / getPortions();
    }

})(jQuery, _, window);