function agent_draw(draw_times){
    var agent_save = $("#js-agent-save").text();
    var agent_times = $("#js-draw-times").text();
    var agent_3 = $("#js-agent-3").text();
    var agent_4 = $("#js-agent-4").text();
    var agent_5 = $("#js-agent-5").text();
    var agent_6 = $("#js-agent-6").text();
    var url = "/ArkNights/draw.html?" + 
            "times=" + draw_times + 
            "&agent_times=" + agent_times +
            "&agent_save=" + agent_save +
            "&agent_3=" + agent_3 +
            "&agent_4=" + agent_4 +
            "&agent_5=" + agent_5 +
            "&agent_6=" + agent_6;
    $.get(url, function(data, status){
        $("#js-draw-main").html(data);
    });
}
$(document).ready(function(){
    $("#js-draw-1").click(function(){
        agent_draw("1");
    });
    $("#js-draw-10").click(function(){
        agent_draw("10");
    });
});