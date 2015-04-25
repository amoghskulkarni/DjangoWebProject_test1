$(document).ready(function () {
    var nameVal = 'Joe';
    var age = 20;

    $("#apply_analysis_btn").click(function (event) {
        alert('Click!');
        $.ajax({
            url: "/applyAnalysis",
            type: "POST",
            data: { 'data': DATA, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value },
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

    $('#postButton').click(function (e) {
        e.preventDefault();
        alert("clicked");
        //      var data = 'Joe is a good boy';
        var DATA = 'test data';
        $.ajax({
            url: "/testPost",
            type: "POST",
            //data: data,
            data: { 'data': DATA, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value },
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
        //});
        //$.post("/testPost", {
        //    testParam : "test Value"
        //}, function (event) {
        //    console.log("success post request!!!");
        //}, function (error) {
        //    console.log("error!!")
        //});
    });
});