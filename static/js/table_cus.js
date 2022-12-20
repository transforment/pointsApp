
$(document).ready(function() {
    $('#tablepaging').DataTable({
        "pagingType": "full",
        "language": {
            "lengthMenu": " {% trans 'Showing' %} _MENU_ {% trans 'mail record' %}",
            "loadingRecords": "{% trans 'Loading' %} ...",
            "search": "{% trans 'Search' %}",
            "paginate": {
                "first": "{% trans 'First' %}",
                "last": "{% trans 'Last' %}",
                "next": '{% trans "Next" %}',
                "previous": "{% trans 'Previous' %}"
            },
            "info": "{% trans 'Showing' %} _START_ -> _END_ {% trans 'of' %} _TOTAL_ {% trans 'mail record' %}",
            "infoFiltered": "",
            "infoEmpty": "No records available",
        }
    });
});