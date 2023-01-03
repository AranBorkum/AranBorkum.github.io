from API.strike_info_endpoint import StrikeEndpoint
from strike_scraper.scrape_engine import ScrapeEngine

from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

api.add_resource(StrikeEndpoint, "/strikes")


if __name__ == "__main__":
    app.run(debug=True, host="localhost")
