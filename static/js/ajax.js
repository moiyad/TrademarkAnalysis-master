$(document).ready(function () {
    $.getJSON("http://127.0.0.1:8000/simple.search/searchResult/", function (data) {
        console.log(data);
        $('#submit_search').click(function () {
            $("#result").empty();
            var value = $("[name=Name]").val();
            for (var i = 0; i < data.length; i++) {
                var name = data[i]['fields']['Name'];
                var product = data[i]['fields']['Product']
                var description = data[i]['fields']['description']
                if (name.toLowerCase().trim().includes(value.toLowerCase().trim())) {
                    $("#result").append(`<table id="t01">
                                                  <tr>
                                                    <th width="20%">Trademark Name</th>
                                                    <th width="20%">Product</th> 
                                                    <th width="60%">Description</th>
                                                  </tr>
                                                  <tr>
                                                    <td>${name}</td>
                                                    <td>${product}</td>
                                                    <td>${description}</td>
                                                  </tr>
                                                  </br>
                                                </table>
                                                `);
                }
            }
        });
    });
});