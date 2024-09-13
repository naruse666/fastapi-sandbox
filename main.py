# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8080",
    "http://localhost"
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
)

router = APIRouter()
router2 = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/error/", tags=["error"])
async def raise_error():
    raise HTTPException(status_code=404, detail="Not Found")
    return ""


@router2.get("/ranking/", tags=["ranking"])
async def read_ranking():
    return [{"rank": "111"}]

app.include_router(router)
app.include_router(router2)
