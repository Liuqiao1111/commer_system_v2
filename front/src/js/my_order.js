var MyOrder = function () {
};

MyOrder.prototype.listenDeleteEvent = function () {
    $(".delete-order-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var order_id = $this.attr('order-id');
        $.ajax({
            url: "/my_order/",
            type: 'POST',
            data: {
                order_id
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


MyOrder.prototype.run = function () {
    this.listenDeleteEvent();
};


$(function () {
    var handler = new MyOrder();
    handler.run();
});