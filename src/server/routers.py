import requests
import fastapi

import src.config


router = fastapi.APIRouter()


@router.get("/redirect-endpoint")
async def redirect_endpoint(code: str, user_id: int, request: fastapi.Request):
    access_token_info = requests.get(
        "https://oauth.vk.com/access_token",
        params={
            "client_id": src.config.CLIENT_ID,
            "client_secret": src.config.CLIENT_SECRET,
            "redirect_uri": request.url,
            "code": code
        }
    )
    return access_token_info.json()