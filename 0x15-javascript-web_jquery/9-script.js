apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr"

data = fetch(apiUrl)
    .then(response => {return response.json()})
        .then(data => {
            $("#hello").ready(function(){
            $("#hello").append(data["hello"])
        })
             

             })
