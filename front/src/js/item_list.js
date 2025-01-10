var ItemList = function () {
};

ItemList.prototype.listenSubmitEvent = function () {
    $(".look-item-detail-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var item_id = $this.attr('item-id');
        window.location = '/item_detail/' + item_id
    });
};

ItemList.prototype.run = function () {
    this.listenSubmitEvent();
};


$(function () {
    var handler = new ItemList();
    handler.run();
});