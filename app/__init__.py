from app import config

from mangum import Mangum
from app.main import app

handler = Mangum(app, api_gateway_base_path=config.ROOT_PATH)