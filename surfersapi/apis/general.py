from fastapi import APIRouter
from surfersapi.config import settings

router = APIRouter(
    prefix="/api/v1",
    tags=["general"],
    responses={404: {"description": "Not found"}},
)

# Status query page, can also be used for the benchmark testing 
@router.get('/healthz')
async def health():
    _status = {
        "health": "ok",
        "environment": settings.ENV,
        "database": settings.DATABASE_URL[:10]
    }
    return _status
