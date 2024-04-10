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
            pass

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
