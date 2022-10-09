import os
from dotenv import load_dotenv
import uvicorn
from surfersapi import create_app
from surfersapi.config import settings
from surfersapi.logger import logger

# Load environment variables
load_dotenv()

logger.info("Starting Application")
# Initialise application context
app = create_app()

_config = settings

if __name__ == "__main__":
    _config = uvicorn.Config(app, host='0.0.0.0', port=_config.USER_PORT, log_level="info")
    _server = uvicorn.Server(_config)
    _server.run()    

