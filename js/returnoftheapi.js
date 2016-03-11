$("#continue").click(function() {
    $("#intro").fadeOut(1000, function() {
        $("#content").fadeIn(1000);
    });
});