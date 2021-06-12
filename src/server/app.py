import uvicorn
import fastapi

import src.server.routers


app = fastapi.FastAPI()
app.api_route(src.server.routers.router)


