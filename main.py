from API.strike_info_endpoint import StrikeEndpoint
from strike_scraper.scrape_engine import ScrapeEngine

from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


api.add_resource(StrikeEndpoint, "/strikes")


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


if __name__ == "__main__":
    app.run(debug=True, host="localhost")
