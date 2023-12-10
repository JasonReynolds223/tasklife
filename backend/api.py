from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from auth.router import router as auth_router
from project.router import router as project_router
# from schedule.router import router as schedule_router
from libs.db import Base, engine, get_db


try:
    Base.metadata.create_all(bind=engine)

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    async def app_startup():
        db = next(get_db())

    @app.on_event("shutdown")
    async def app_shutdown():
        await app.state.redis.close()

    apis_router = APIRouter(prefix="/api")

    apis_router.include_router(auth_router)
    apis_router.include_router(project_router)
    # apis_router.include_router(schedule_router)
    app.include_router(apis_router)
    
except ValueError as error:
    print("ERROR", error)
