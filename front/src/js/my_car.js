var MyCar = function () {
};

MyCar.prototype.listenDeleteEvent = function () {
    $(".delete-car-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var car_id = $this.attr('car-id');
        $.ajax({
            url: "/my_car/",
            type: 'POST',
            data: {
                car_id
            },
            success: function (result) {
                if (result['code'] == 200) {
                    alert('删除成功');
                    location.reload()
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};

MyCar.prototype.listenAddOrderEvent = function () {
    $(".add-order-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var car_id = $this.attr('car-id');
        var item_id = $this.attr('item-id');
        $.ajax({
            url: "/add_order/",
            type: 'POST',
            data: {
                car_id,
                item_id
            },
            success: function (result) {
                if (result['code'] == 200) {
                    alert('购买成功');
                    location.reload();
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};

MyCar.prototype.run = function () {
    this.listenDeleteEvent();
    this.listenAddOrderEvent();
};


$(function () {
    var handler = new MyCar();
    handler.run();
});