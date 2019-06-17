function find_html_block(html_data, block_name){
    block_name_fixed = "<!-- " + block_name + " -->";
    for(var i = 0; i < html_data.length - (8 + block_name.length); i++){
        if(html_data[i] == '<'){
            if(html_data.substring(i, i + 9 + block_name.length) == block_name_fixed){
                return i;
            }
        }
    }
    return -1;
}

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
    alert(url)
    $.get(url, function(data, status){
        var pos = find_html_block(data, "js-stat-show");
        $("#js-draw-show").html(data.substring(0, pos));
        $("#js-stat-show").html(data.substring(pos));
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