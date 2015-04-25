$(document).ready(function () {

    $('#suggButton').click(function (e) {
        e.preventDefault();
        //get radio button values
        var size = $('input:radio[name=size]:checked').val();
        var categorical = $('input:radio[name=categorical]:checked').val();
        var labelled = $('input:radio[name=labelled]:checked').val();
        var numClusters = $('input:radio[name=numClusters]:checked').val();
        if (!$("input[name=size]:checked").val()) {
            alert('Please answer all the questions!');
        }
        else if (!$("input[name=categorical]:checked").val()) {
            alert('Please answer all the questions!');
        }
        else if (!$("input[name=labelled]:checked").val()) {
            alert('Please answer all the questions!');
        }
        else if (!$("input[name=size]:numClusters").val()) {
            alert('Please answer all the questions!');
        }
        else{
            alert("inside this block");
            alert(String(size));
            alert(String(categorical));
            alert(String(labelled));
            alert(String(numClusters));
            var DATA = size + "," + categorical+ "," + labelled + "," + numClusters;
            alert(DATA)
            $.ajax({
                url: "/testImageResponse",
                type: "POST",
                //data: data,
                data: { 'data': DATA, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value },
                success: function (response) {
                    alert("In success. Got - " + response);
                },
                complete: function (response) {
                    document.getElementById('imageDiv').style.backgroundImage = response //incorrect line
                },
                error: function (xhr, textStatus, thrownError) {
                    alert("error doing something");
                }
            });
    }
    });

});