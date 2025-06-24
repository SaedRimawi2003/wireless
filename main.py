from fastapi import FastAPI
from routes.link_budget_api import router as link_budget_router
from routes.ofdm_api import router as ofdm_router
from routes.wireless_api import router as wireless_router
from routes.cellular_api import router as cellular_router
from routes.ai_explain_api import router as ai_explain_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="Wireless & Mobile Network Design API",
    description="An AI-powered backend for wireless design calculations.",
    version="1.0"
)

# Serve frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Homepage route (returns index.html)
@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

# Include routers
app.include_router(link_budget_router, prefix="/api")
app.include_router(ofdm_router, prefix="/api")
app.include_router(wireless_router, prefix="/api")
app.include_router(cellular_router, prefix="/api")
app.include_router(ai_explain_router, prefix="/api")
