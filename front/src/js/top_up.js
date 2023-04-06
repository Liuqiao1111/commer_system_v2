var TopUp = function () {
};

TopUp.prototype.listenSubmitEvent = function () {
    $("#submit-btn").on("click", function (event) {
        event.preventDefault();
        var money = $("#money").val();
        $.ajax({
            url: "/top_up/",
            type: 'POST',
            data: {
                money
            },
            success: function (result) {
                if (result['code'] == 200) {
                    alert('充值成功');
                    location.reload()
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};

TopUp.prototype.run = function () {
    this.listenSubmitEvent();
};


$(function () {
    var handler = new TopUp();
    handler.run();
});