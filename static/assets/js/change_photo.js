var image_id = 0;
var product_id = 0;

function send_val(item_id, pro_id) {

    image_id = item_id;
    product_id = pro_id;
    console.log(item_id)


    var token = $("input[name=csrfmiddlewaretoken]").val();


    $.ajax({
        method: 'POST',
        url: "/shop-images/",
        data: {
            "product_id": product_id,
            "image_id": image_id,
            csrfmiddlewaretoken: token
        },
        success: function (response) {

            console.log(response)

        }
    })
}
