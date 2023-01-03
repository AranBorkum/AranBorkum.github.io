const requestUrl = "http://localhost:5000/strikes";

function getData(requestUrl) {

    fetch(requestUrl)
        .then(res => res.json())
        .then((data) => {
            data.results.forEach((string) => {
                console.log(string);
            });
        });
}

getData(requestUrl)


