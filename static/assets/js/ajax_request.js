var size = undefined
var product_image = undefined
var variant = undefined
$(".size_class li").on("click", function () {
    size = $(this).text();

});

$("#color_class li").on("click", function () {
    // product_image =  document.getElementById("image_id").value;
    product_image = $(this).text();

});

$(".variant_class li").on("click", function () {
    variant = $(this).text();
});

$('.addToCartBtn').on('click', function () {
    var product_id = $('.prod_id').val()
    var quantity = $('.qty-input').val()
    var token = $("input[name=csrfmiddlewaretoken]").val();


    $.ajax({
        method: 'POST',
        url: "/order/add-to-cart/",
        data: {
            "product_id": product_id,
            "quantity": quantity,
            "size": size,
            "variant": variant,
            "product_image": product_image,
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            if (response.status) {
                alertify.success(response.msg)
                location.reload();
            } else {
                alertify.error(response.msg)
            }
        }
    })

})

