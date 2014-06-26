(function($, _, global) {
    var selectorProductWeightInput = '.product-weight-field input',
        selectorStatisticsWeight = '#statistics-weight';

    function getProductsWeight() {
        var weight = 0, productWeight;
        _.each($(selectorProductWeightInput), function(inputEl) {
            productWeight = parseInt(inputEl.value);
            if (productWeight) {
                weight += productWeight;
            }
        });

        return weight;
    }


    function updateStatisticsWeight() {
        $(selectorStatisticsWeight).html(getProductsWeight());
    }


    global.Diabetto = global.Diabetto || {};
    global.Diabetto.Statistics = {
        updateStatistics: function() {
            updateStatisticsWeight();
        }
    };

})(jQuery, _, window);