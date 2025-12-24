from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/")
def Hello_sai():
    return {"Hello": "SAI"}

