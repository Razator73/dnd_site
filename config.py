from dotenv import load_dotenv
from dynaconf import Dynaconf

load_dotenv()

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
    environment=True
)


class AppConfig(object):
    SECRET_KEY = settings.secret_key
    SQLALCHEMY_DATABASE_URI = settings.db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = settings.db_track_modifications

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
