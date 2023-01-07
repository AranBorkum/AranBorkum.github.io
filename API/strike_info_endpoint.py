from flask_restful import Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db.strikes import Strikes


DB_URI = "postgresql://strikes_db:strikes_db@localhost:5432/postgres"


class StrikeEndpoint(Resource):
    @staticmethod
    def get():
        data = {
            "strikes": [],
        }

        with Session(create_engine(DB_URI)) as session:
            future_strikes = session.query(Strikes)
            # .filter(
            #     Strikes.date_of_strike > datetime.datetime.now()
            # )

            for element in future_strikes:
                data["strikes"].append(
                    {
                        "id": str(element.id),
                        "date_of_strike": str(element.date_of_strike),
                        "strike_message": element.strike_message,
                        "date_added_to_db": str(element.date_added_to_db),
                    }
                )

        return {"data": data}, 200


if __name__ == "__main__":
    se = StrikeEndpoint()
    se.get()
