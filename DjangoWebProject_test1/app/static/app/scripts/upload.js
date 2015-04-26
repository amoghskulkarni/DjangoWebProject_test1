$(document).ready(function () {

    $('#apply_analysis_btn').click(function (event) {
        event.preventDefault();
        alert('Click!');
        $.ajax({
            url: "/applyAnalysis",
            type: "POST",
            data: { 'data': $("#analysis_list").val(), csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value },
            success: function (response) {
                // alert("In success. Got - " + response);
                // $('#imagediv').html('<img alt="Embedded Image" src="data:image/png;base64,' + response + '" />');
                // $('#imagediv').html('<img src=' + window.URL.createObjectURL(response) + ' />');
                // $('#imagediv').html('<img src=' + response + ' />');
                // $("#imagediv").html("<img src=" + window.URL.createObjectURL(new Blob([response], { "type": "image/png" })) + "/>");
                // $('#imagediv').html('<img alt="Embedded Image" src="data:image/png;base64,' + window.URL.createObjectURL(new Blob([response], { "type": "image/png" })) + '" />');
                // $('#image').attr('src', 'data:image/png;base64,' + response);

                var reader = new FileReader();
                reader.onload = function (e) {
                    $("#imagediv").html("<img src=" + e.target.result + "/>");
                };
                reader.readAsDataURL(response);
                
                alert("In success.");
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