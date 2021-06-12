import uvicorn
import fastapi


app = fastapi.FastAPI()


@app.get("/redirect-endpoint")
async def redirect_endpoint(code: str):
    print(code)


uvicorn.run(app, host="185.119.58.249", port=9000)