import uvicorn

import src.server.app
import src.config


uvicorn.run(
    src.server.app.app,
    host=src.config.SERVER_IP,
    port=src.config.SERVER_PORT
)
