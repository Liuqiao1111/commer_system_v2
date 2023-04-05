var ItemDetail = function () {
};

ItemDetail.prototype.listenAddCar = function () {
    $("#add-car-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var item_id = $this.attr('item-id');

        $.ajax({
            url: "/add_car/",
            type: 'POST',
            data: {
                item_id
            },
            success: function (result) {
                if (result['code'] == 200) {
                    alert('加入成功');
                    location.reload()
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};


ItemDetail.prototype.listenAddOrder = function () {
    $("#add-order-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var item_id = $this.attr('item-id');

        $.ajax({
            url: "/add_order/",
            type: 'POST',
            data: {
                item_id
            },
            success: function (result) {
                if (result['code'] == 200) {
                    alert('购买成功');
                    location.reload()
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};


ItemDetail.prototype.run = function () {
    this.listenAddCar();
    this.listenAddOrder();
};


$(function () {
    var handler = new ItemDetail();
    handler.run();
});