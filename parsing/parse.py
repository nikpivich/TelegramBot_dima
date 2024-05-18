import json
import datetime
import config
import requests
def day():
    weather_key = 'ZRBUWXMFZAAT93AS8UMT5JV6S'

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Minsk,Belarus/{datetime.date.today()}?key={weather_key}"
    response = requests.get(url).json()
    new = response.get('days')
    for item in new:
        tmin = str(item.get('tempmin'))
        wspeed = str(item.get('windspeed'))
        tmax = str(item.get('tempmax'))
        list1 = [str(round((float(tmin) - 32) * 5/9)) ,wspeed,str(round((float(tmax) - 32) * 5/9))]
        print(datetime.datetime.now())
        print(str(tmin) + ' Минимальная температура')
        print(wspeed + ' Скорость ветра')
        print(tmax + ' Максимальная температура')
        return list1


#day()




#info_days(data=response)

#day(data=response)






#
#
#
# with open('data.json', 'w', encoding='UTF-8') as f:
#     json.dump(response, f, ensure_ascii=False, indent=4)