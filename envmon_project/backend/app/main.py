from fastapi import FastAPI
from . import routes

app = FastAPI(title="Environmental Monitoring API")
app.include_router(routes.router)
