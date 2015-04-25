$(document).ready(function () {

    $('#suggButton').click(function (e) {
        e.preventDefault();

        // Get radio button values
        var size = $('input:radio[name=size]:checked').val();
        var categorical = $('input:radio[name=categorical]:checked').val();
        var labelled = $('input:radio[name=labelled]:checked').val();
        var numClusters = $('input:radio[name=numClusters]:checked').val();

        if ((typeof size === "undefined") || (typeof categorical === "undefined") || (typeof labelled === "undefined") || (typeof numClusters === "undefined")) {
            alert('Please answer all the questions!');
        }
        else {
            var DATA = size + "," + categorical + "," + labelled + "," + numClusters;
            // alert(DATA);
            $.ajax({
                url: "/suggestions",
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