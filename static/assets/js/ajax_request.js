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

$('.addToCartBtn').on('click', function (e) {
    e.preventDefault();
    var product_id = $('.prod_id').val()
    var quantity = $('.qty-input').val()
    var token = $("input[name=csrfmiddlewaretoken]").val();
	const extractDjangoLanguage = document.cookie.match(/django_language=([^;]+)/);
	const currLanguage = extractDjangoLanguage !== null ? extractDjangoLanguage[1] : "ru"

    $.ajax({
        method: 'POST',
        url: `/${currLanguage}/order/add-to-cart/`,
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
                document.location.reload();
            } else {
                alertify.error(response.msg)
            }
        }
    })

})

