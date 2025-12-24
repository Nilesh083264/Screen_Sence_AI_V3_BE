from fastapi import APIRouter
from api.controller_apis.sai import router as Hello_sai_api
from api.controller_apis.nilesh import router as nilesh_api

router = APIRouter()


router.include_router(Hello_sai_api)
router.include_router(nilesh_api)
