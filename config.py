from dataclasses import dataclass

from dotenv import dotenv_values, load_dotenv

ENV_FILENAME = "secrets/.local.env"
load_dotenv(ENV_FILENAME)


def get_values(env_filename: str) -> dict:
    return dotenv_values(env_filename)


# @dataclass
# class Config:
#
#     ENV_FILENAME = "secrets/.local.env"
#     load_dotenv(ENV_FILENAME)
#
#     DB_HOST = dotenv_values(ENV_FILENAME)["DB_HOST"]
#     DB_NAME = dotenv_values(ENV_FILENAME)["DB_NAME"]
#     DB_PASS = dotenv_values(ENV_FILENAME)["DB_PASS"]
#     DB_PORT = dotenv_values(ENV_FILENAME)["DB_PORT"]
#     DB_USER = dotenv_values(ENV_FILENAME)["DB_USER"]
#     DB_URI = "{driver}://{username}:{password}@{host}:{port}/{dbname}".format(
#         driver="postgresql",
#         username=DB_USER,
#         password=DB_PASS,
#         host=DB_HOST,
#         port=DB_PORT,
#         dbname=DB_NAME,
#     )


if __name__ == "__main__":
    config = Config()
    print(config.DB_URI)
