import uvicorn
import fastapi

import src.server.routers


app = fastapi.FastAPI()
app.include_router(src.server.routers.router)


