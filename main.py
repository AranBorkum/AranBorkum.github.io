from strike_scraper.scrape_engine import ScrapeEngine

from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

engine = ScrapeEngine()
engine.get_list_elements()
