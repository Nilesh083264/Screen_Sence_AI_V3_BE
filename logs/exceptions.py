from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

def json_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Invalid JSON",
            "detail": str(exc)
        }
    )
