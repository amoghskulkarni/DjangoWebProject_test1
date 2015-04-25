$(document).ready(function () {

    $('#apply_analysis_btn').click(function (event) {
        event.preventDefault();
        alert('Click!');
        $.ajax({
            url: "/applyAnalysis",
            type: "POST",
            data: { 'data': $("#analysis_list").val(), csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value },
            success: function (response) {
                alert("In success. Got - " + response);
            },
            complete: function (response) {
                alert("In complete. Got - " + response);
            },
            error: function (xhr, textStatus, thrownError) {
                alert("error doing something");
            }
        });
    });

});