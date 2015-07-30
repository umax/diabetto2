(function($, _, global) {
    var selectorStatisticsWeightPerPortion = '#statistics-weight-per-portion',
        selectorStatisticsCarbohydrateUnits = '#statistics-carbohydrate-units',
        selectorStatisticsCarbohydrateUnitsPerPortion = '#statistics-carbohydrate-units-per-portion',

        selectorProductLi = 'li[data-product-id]',
        selectorProductsList = '#products-list',
        selectorPortonsInput = '#id_portions';
        selectorDishWeightInput = '.statistics-dish-weight-input',


    global.Diabetto = global.Diabetto || {};
    global.Diabetto.Statistics = {
        updateStatistics: function() {
            Statistics = global.Diabetto.Statistics;

            Statistics.updateStatisticsCarbohydrateUnits();
            Statistics.updateStatisticsCarbohydratePerPortion();
            Statistics.updateStatisticsWeightPerPortion();
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


    function getWeight() {
        return parseInt($(selectorDishWeightInput).val());
    }


    function getProductsWeightPerPortion() {
        /* Calculate all added products weight per portion */

        var portions = getPortions();
        if (portions) {
            return getWeight() / portions;
        }
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

            if (productWeight) {
                carbohydrateUnits += (productCarbohydrates / 100.0 * productWeight / 12);
            }
        });

        return carbohydrateUnits;
    }


    function getCarbohydrateUnitsPerPortion() {
        /* Calculate all added products carbohydrate units per portion */

        var portions = getPortions();
        if (portions) {
            return getCarbohydrateUnits() / portions;
        }
    }

    $(document).ready(function() {
        $(selectorDishWeightInput).keyup(
            global.Diabetto.Statistics.updateStatisticsWeightPerPortion);
    });

})(jQuery, _, window);
