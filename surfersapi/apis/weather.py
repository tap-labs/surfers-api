from fastapi import APIRouter
from surfersapi.services import feeds
from surfersapi.services.bom import observations, locationsearch

router = APIRouter(
    prefix="/api/v1/weather",
    tags=["weather"],
    responses={404: {"description": "Not found"}},
)

@router.get('/alert')
def alert():
    _alert = feeds.getWeather()
    '''Get weather alerts'''
    alert_example = [
        {
            'title': 'Heavy wind alert NSW',
            'location': 'New South Wales',
            'published': 'some time details',
            'link': 'http://somewhere.weather.com'
        },
    ]
    return _alert
 

@router.get('/observation/{geotag}')
async def observation(geotag: str):
    _observations = observations(geotag)
    '''Get current observed weather from location identifier'''
    return _observations



@router.get('/locations/{searchstring}')
async def locations(searchstring):
    _locations = locationsearch(searchstring)
    return _locations

