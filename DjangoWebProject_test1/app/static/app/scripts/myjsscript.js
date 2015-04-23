$(document).ready(function () {
    var nameVal = 'Joe';
    var age = 20;
    $("#mybutton").click(function (event) {
        //var res = $.get("/myrequest", "Hello!",
        //function (data, status) {
        //    alert("Data: " + data + "\nStatus: " + status);
        //});
        alert("Click!");
        // var res = $.get("/helloworld");
        // alert(res.value);
    });
    $('#postButton').click(function (e) {
        e.preventDefault();
        alert("clicked");
        var data = 'Joe is a good boy';
        var age = 20;
        $.ajax({
            url:"/testPost",
            type: "POST",
            data: data,
            success: function (response) {
                alert("In success. Got - " + response);
            },
            complete: function (response) {
                alert("In complete. Got - " + response);
            },
            error:function (xhr, textStatus, thrownError){
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