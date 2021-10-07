import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls) -> bool:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric')
        
        if response.status_code == 200:
            content = response.json()
            temp = content['main']['temp']
            if temp > 28:
                return True
        return False


print(GeoAPI.is_hot_in_pehuajo())
