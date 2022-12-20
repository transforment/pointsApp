function person_checkbox(idPersonnel) {
    var personnel_list = document.getElementById("personnel_list").value;
    var replace = "," + idPersonnel.replace("per_", "");
    personnel_list = personnel_list.replace(replace, "");
    if (document.getElementById(idPersonnel).checked == true) {
        personnel_list = personnel_list + "," + idPersonnel.replace("per_", "");
    }
    document.getElementById("personnel_list").value = personnel_list;
    checkstt();
    console.log(personnel_list);
}

function job_checkbox(idJob) {
    var job_list = document.getElementById("job_list").value;
    var replace = "," + idJob.replace("job_", "");
    job_list = job_list.replace(replace, "");
    if (document.getElementById(idJob).checked == true) {
        job_list = job_list + "," + idJob.replace("job_", "");
    }
    document.getElementById("job_list").value = job_list;
    checkstt();
    console.log(job_list);
}

function checkstt() {
    if ((document.getElementById("personnel_list").value == "") || (document.getElementById("job_list").value == "")) {
        document.getElementById("matching_submit").disabled = true;
    } else {
        document.getElementById("matching_submit").disabled = false;
    }
}
$(document).ready(function() {
    $("#person_select_all").click(function() {
        if ($('.person_record').length == $('.person_record:checkbox:checked').length) {
            $('.person_record').prop('checked', false).change();
            $('#dvcount').html($('.person_record:checkbox:checked').length);
        } else {
            $('.person_record').prop('checked', true).change();
            var idPersonnel = this.id;
            $('#dvcount').html($('.person_record:checkbox:checked').length);
        }
    });
    $("#job_select_all").click(function() {
        if ($('.job_record').length == $('.job_record:checkbox:checked').length) {
            $('.job_record').prop('checked', false).change();
            $('#dvcount').html($('.job_record:checkbox:checked').length);
        } else {
            $('.job_record').prop('checked', true).change();
            var idPersonnel = this.id;
            $('#dvcount').html($('.job_record:checkbox:checked').length);
        }
    });
    $('[data-toggle="popover"]').popover({
        placement : 'top',
        trigger : 'hover'
    });
});