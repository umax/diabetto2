(function($, _) {

    $(document).ready(function() {
        var productsList = $('#products-list'),
            productTemplate = _.template($('#product-template').text());

        _.each(window.Diabetto.dishProducts, function(product) {
            var productEl = $(productTemplate({
                'productId': product.id,
                'productName': product.name,
                'productWeight': product.weight
            }));
            productsList.append(productEl).listview('refresh');
        });
    });

})(jQuery, _);