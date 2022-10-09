from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/surf",
    tags=["surf"],
    responses={404: {"description": "Not found"}},
)


swell_example = [
    {
        'height': 6,
        'interval': 11,
        'direction': 'SE'
    },
]


water_example = [
    {'temperature': 22},
]


@router.get('/swell/{location_id}')
async def swell(location_id: str):
    if location_id:
        '''Get swell forecast from location identifier'''
        return swell_example
