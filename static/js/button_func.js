$(".label_text").val('default');
$(".label_text").selectpicker("refresh");


$('#progressBarModal').on('shown.bs.modal', function() {
    //var progress = setInterval(function() {
        // $('#progressBarModal').modal('hide');
        // perform processing logic here
    //}, 5000);
})
$(document).ready(function() {

    $('[data-toggle="tooltip"]').tooltip();
    if (document.getElementById("inputTextToWrite")) {
        document.getElementById("inputTextToWrite").value = ""
    }
       $("select.label_text").change(function(){
        var selectId = this.id;
        var numId = selectId.split("_")[1];
        var textId= "textId_" + numId;
        var text = document.getElementById(textId).innerText;
        var pre_line = document.getElementById("inputTextToWrite").value
        var label_temp = $(this).find("option:selected").text().replace(/ /g, " __label__");
        var line = label_temp.trim() + " " + text;
        var pos = pre_line.indexOf(text);
        var i;
        var replace_string;
        if (pos == -1) {
            console.log("them dong")
            if ($(this).find("option:selected").text() != ""){
                document.getElementById("inputTextToWrite").value = pre_line + "\n" + line;
            }
            console.log(pre_line)
        } else {
            var pre_lines = pre_line.split("\n");
            for (i = 0; i < pre_lines.length; i++) {
                var pre =pre_lines[i].split(" ");
                var k;
                var remove_label= pre_lines[i];
                for (k = 0; k < pre.length; k++) {
                    if (pre[k].indexOf("__label__") != -1){
                        remove_label = remove_label.replace(pre[k], "");
                    }
                }
                if ( remove_label.trim() == text) {
                    replace_string = pre_lines[i];
                    break;
                }
            }
            if ($(this).find("option:selected").text() == ""){
                pre_line = pre_line.replace(replace_string, "");
            }else{
                pre_line = pre_line.replace(replace_string, line);

            }
            pre_line = pre_line.replace(/^\s*\n/gm, "");
            document.getElementById("inputTextToWrite").value = pre_line;
        }
        console.log(pre_line)

    });

    $('#filldata').bind('click', function(e) {
        console.log("fffffff");
    });
});