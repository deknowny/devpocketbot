import fastapi


app = fastapi.FastAPI()


@app.route("/redirect-endpoint")
async def redirect_endpoint(code: str):
    print(code)