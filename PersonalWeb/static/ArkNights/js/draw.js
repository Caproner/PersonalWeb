$(document).ready(function(){
    $("#js-draw-1").click(function(){
        $.get("/ArkNights/draw.html?times=1", function(data, status){
            $("#js-draw-show").html(data);
        });
    });
    $("#js-draw-10").click(function(){
        $.get("/ArkNights/draw.html?times=10", function(data, status){
            $("#js-draw-show").html(data);
        });
    });
});