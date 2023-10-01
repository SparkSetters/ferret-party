from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)


@router.get("/test")
async def test_response():
    return [{"username": "Rick"}, {"username": "Morty"}]
