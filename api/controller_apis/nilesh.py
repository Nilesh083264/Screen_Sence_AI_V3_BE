from fastapi import APIRouter, HTTPException, Request

router = APIRouter()

@router.post("/urls")
async def hello_nilesh(request: Request):
    try:
        data = await request.json()
        print("data:", data)
        return {"Nilesh": data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")
