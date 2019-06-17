function agent_draw(draw_times){
    alert("!!!!!")
    var agent_save = $("#js-agent-save").val();
    var agent_times = $("#js-agent-times").val();
    var agent_3 = $("#js-agent-3").val();
    var agent_4 = $("#js-agent-4").val();
    var agent_5 = $("#js-agent-5").val();
    var agent_6 = $("#js-agent-6").val();
    $.get("/ArkNights/draw.html?" + 
            "times=" + draw_times + 
            "&agent_times=" + agent_times +
            "&agent_save=" + agent_save +
            "&agent_3=" + agent_3 +
            "&agent_4=" + agent_4 +
            "&agent_5=" + agent_5 +
            "&agent_6=" + agent_6
            , function(data, status){
        $("#js-draw-show").html(data);
        $("#js-agent-times").val(agent_times);
        $("#js-agent-save").val(agent_save);
        $("#js-agent-3").val(agent_3);
        $("#js-agent-4").val(agent_4);
        $("#js-agent-5").val(agent_5);
        $("#js-agent-6").val(agent_6);
    });
}
$(document).ready(function(){
    $("#js-draw-1").click(function(){
        agent_draw('1');
    });
    $("#js-draw-10").click(function(){
        agent_draw('10');
    });
});