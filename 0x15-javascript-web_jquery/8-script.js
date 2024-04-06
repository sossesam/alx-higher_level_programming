apiUrl = "https://swapi-api.alx-tools.com/api/films/?format=json"

data = fetch(apiUrl)
    .then(response => {return response.json()})
        .then(data => {
            $("#list_movies").ready(function(){
            for(i = 0; i < data["count"]; i++){
                
                    $("#list_movies").append("<p>"+ data["results"][i]["title"] +"</p>")
    
            }
        })
             

             })
