apiUrl = "https://swapi-api.alx-tools.com/api/people/5/?"

data = fetch(apiUrl)
    .then(response => {return response.json()})
        .then(data => {

            $("#character").ready(function(){
                $("#character").append("<p>" + data["name"] + "<p>")
                })

             })
