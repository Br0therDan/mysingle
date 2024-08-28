# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1 import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG,
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# v1 API 라우터 포함
app.include_router(api_router, prefix="/api/v1")

# 이벤트 핸들러 (옵션)
@app.on_event("startup")
async def startup_event():
    # 앱이 시작할 때 수행할 작업을 여기에 추가하세요.
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # 앱이 종료될 때 수행할 작업을 여기에 추가하세요.
    pass

# 기본 경로
@app.get("/")
async def root():
    return {"message": "Welcome to MySingle API!"}