import requests

name = input('Введите имя: ')
while True:
    text = input('Введите сообщение: ')
    if text.startswith('/'):
        text = text[1:]
        text = text.rstrip()

        if text == "help":
            print("Список команд:\n/help\n/weather\n/anon\n/deanon")

        elif text == "weather":
            url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {'lat':55.751244, 'lon':37.618423, 'appid': '8537d9ef6386cb97156fd47d832f479c', 'units': 'metric'}
            response = requests.get(url, params=params)
            data = response.json()
            city = str(data['name'])
            temp = str(data['main']['temp'])
            feels_like = str(data['main']['feels_like'])
            print("Температура в " + city + " " + temp + " градусов, ощущается как " + feels_like + " градусов")

        elif text == "anon":
            name = "Аноним"
            print("Ваши сообщения теперь анонимны, для отмены операции введите /deanon")

        elif text == "deanon":
            name = input('Введите имя: ')

        else:
            print("Такой команды нет, список команд:\n/help\n/weather\n/anon\n/deanon")
            
    else:
        response = requests.post('http://127.0.0.1:5000/send',
                                json={
                                'name': name,
                                'text': text
                                }
                            )
