var type_data = {
    variant: 0,
    image: 0,
};
function calculate(duration, percent, price, status, id) {
    if (status === "images") {
        type_data.image = {
            id: id,
            price: price,
            temp_price: price,
        }
        if (type_data.variant === 0) {
            var image_total = price + ((percent * price) / 100);
            var image_monthly = image_total / duration;
            image_monthly = Math.trunc(image_monthly);
            type_data.image.temp_price = Math.trunc(image_total).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
            type_data.image.price = price

        } else {
            var image_total = price + ((type_data.variant.percent * price) / 100);
            var image_monthly = image_total / type_data.variant.duration;
            image_monthly = Math.trunc(image_monthly);
            type_data.image.temp_price = Math.trunc(image_total).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
            type_data.image.price = price
        }
        image_monthly = Math.trunc(image_monthly).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
        image_monthly = image_monthly + " uzs/oy";
        price = type_data.image.temp_price + " uzs";
        $("#monthly").text(image_monthly);
        $("#origin_price").text(price);
    } else {
        type_data.variant = {
            id: duration.id,
            duration: duration.duration,
            percent: duration.percent
        }

        if (type_data.image === 0) {
            var total = parseFloat(duration.price) + ((duration.percent * parseFloat(duration.price)) / 100);
            var monthly = total / duration.duration;
            monthly = monthly.toFixed(2);
            price = Math.trunc(total).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " uzs";
        } else {
            var total = parseFloat(type_data.image.price) + ((duration.percent * parseFloat(type_data.image.price)) / 100);
            var monthly = total / duration.duration;
            monthly = Math.trunc(monthly);
            price = Math.trunc(total).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " uzs";
        }
        monthly = Math.trunc(monthly).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
        monthly = monthly + " uzs/oy";

        $("#monthly").text(monthly);
        $("#origin_price").text(price);
    }
}

// ================================================ Banner Deadline ====================================================

const eventBox = document.getElementById('event-box');
const dayBox = document.getElementById('day');
const hourBox = document.getElementById('hour');
const minBox = document.getElementById('min');
const secBox = document.getElementById('sec');
// console.log(eventBox.textContent);

const evenDate = Date.parse(eventBox.textContent);
// console.log(evenDate);

setInterval(() => {
    const now = new Date().getTime();
    // console.log(now);

    const diff = evenDate - now;
    // console.log(diff);

    const d = Math.floor(evenDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)));
    const h = Math.floor((evenDate / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24);
    const m = Math.floor((evenDate / (1000 * 60) - (now / (1000 * 60))) % 60);
    const s = Math.floor((evenDate / (1000) - (now / (1000))) % 60);
    // console.log(m);
    // console.log(s);

    if (diff >= 0) {
        // countdownBox.innerHTML = `${d.toString().padStart(2, '0')} : ${h.toString().padStart(2, '0')} : ${m.toString().padStart(2, '0')} : ${s.toString().padStart(2, '0')}`;
        dayBox.innerHTML = `${d.toString().padStart(2, '0')}`;
        hourBox.innerHTML = `${h.toString().padStart(2, '0')}`;
        minBox.innerHTML = `${m.toString().padStart(2, '0')}`;
        secBox.innerHTML = `${s.toString().padStart(2, '0')}`;
        // console.log(countdownBox.innerHTML);
    }

}, 1000);



