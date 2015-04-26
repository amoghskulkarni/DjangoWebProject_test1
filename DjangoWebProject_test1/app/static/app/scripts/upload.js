$(document).ready(function () {

    $('#apply_analysis_btn').click(function (event) {
        event.preventDefault();
        alert('Click!');
        $.ajax({
            url: "/applyAnalysis",
            type: "POST",
            data: { 'datafile': $("#uploaded_files_list").val(), 'analysis': $("#analysis_list").val(), csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value },
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

    $('#show_text_btn').click(function (event) {
        event.preventDefault();
        alert('Click!');
        $.ajax({
            url: "/showText",
            type: "POST",
            data: { 'datafile': $("#uploaded_files_list").val(), 'analysis': $("#analysis_list").val(), csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value },
            success: function (response) {
                $('#textdiv').html(response);
            },
            complete: function (response) {
                alert("In complete. Got - " + response);
            },
            error: function (xhr, textStatus, thrownError) {
                alert("error doing something");
            }
        });
    });

    $('#show_img_btn').click(function (event) {
        event.preventDefault();
        alert('Click!');
        $.ajax({
            url: "/showImage",
            type: "POST",
            data: { 'datafile': $("#uploaded_files_list").val(), 'analysis': $("#analysis_list").val(), csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value },
            success: function (response) {
                $('#imagediv').html('<img src="data:image/png;base64,' + response + '" />');
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