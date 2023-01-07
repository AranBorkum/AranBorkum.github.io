const webpage = document.getElementById("root");

const container = document.createElement("div");
container.setAttribute("class", "container");

webpage.appendChild(container);

let request = new XMLHttpRequest();
request.open("GET", "http://localhost:5000/strikes", true);
request.onload = function () {

    let data = JSON.parse(this.response);

    if (request.status >= 200 && request.status < 400) {
        data.data.strikes.forEach(strike_message => {
            console.log(strike_message);

            const message = document.createElement("div");
            message.setAttribute("class", "message");

            const p = document.createElement("p");
            p.textContent = strike_message.date_of_strike + ": " + strike_message.strike_message;

            message.appendChild(p);
            container.appendChild(message)
        });
    } else {
        const errorMessage = document.createElement("marquee");
        errorMessage.textContent = "Why is this not working?";
        webpage.appendChild(errorMessage);
    }
}

request.send();