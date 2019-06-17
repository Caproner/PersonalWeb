$(document).ready(function(){
    $("#draw-10").click(function(){
        $.get("/ArkNights/draw.html?times=10", function(data, status){
            $("#js-draw-show").html(data);
        });
    });
});