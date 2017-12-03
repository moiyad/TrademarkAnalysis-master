$(document).ready(function () {
    $.getJSON("http://127.0.0.1:8000/simple.search/searchResult/", function (data) {
        console.log(data);
        $('#submit_search').click(function () {
            $("#result").empty();
            var value = $("[name=Name]").val();
            for(var i =0;i<data.length;i++){
                var name = data[i]['fields']['Name'];
                if(name.toLowerCase().trim().includes(value.toLowerCase().trim())){
                    $("#result").append(`<li>${name}</li>`);
                }
            }
        });
    });
});