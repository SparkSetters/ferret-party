import os
from fastapi import Depends, FastAPI, HTTPException, Request
from jose import JWTError, jwt
from routers import test
# from dotenv import load_dotenv

# # Load .env file (if you're using one)
# load_dotenv()

JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
ALGORITHM = os.getenv("SUPABASE_JWT_ALGORITHM")


def get_current_user(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(
            status_code=401, detail="Authorization header missing")

    token = token.split("Bearer ")[-1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid JWT token")


app = FastAPI(dependencies=[Depends(get_current_user)])

app.include_router(test.router)


@app.get("/")
def read_root():
    return {"Hello": "World!"}
