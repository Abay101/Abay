import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import pyowm
import datetime
import time
import random
from yandex import Yandex
owm = pyowm.OWM('f58349d7f89f82766b104bc8b3f318b1',language='ru')
tr = Yandex("trnsl.1.1.20200330T093309Z.78fec69e39693730.547031818e28482d613b74094fe05dde97fe1423")

#cmds = {
      #"ctime": ('текущее время','сейчас времени', 'который час'),
      #"radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
      #"stupid1": ('расскажи анекдот', 'рассмещи меня', 'ты знаешь анекдот')
      #}
a = random.randint(1, 3)
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
engine = pyttsx3.init()
def talk(words):
    print(words)
    engine.say(words)
    engine.runAndWait()
talk('Здравствуйте, попросите что-нибудь : ')

def commands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Говорите : ')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        exersize = r.recognize_google(audio, language="ru-Ru").lower()
        print('Вы сказали : ' + exersize)
    except sr.UnknownValueError:
        talk('Я вас не поняла , повторите пожалуйста ')
        exersize = commands()

    return exersize

def makeSomeThing(exersize):
    if 'открой гугл' in exersize:
        talk('Сию минуту' )
        url = 'https://www.google.com/'
        webbrowser.get('Chrome').open_new_tab(url)
        
    elif 'какое твое имя' in exersize or 'как тебя зовут' in exersize:
        talk('Меня зовут Данелия')
    elif 'текущее время' in exersize or 'сейчас времени' in exersize or 'который час' in exersize:
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ':' + str(now.minute))
    elif 'топ' in exersize or 'стоп' in exersize or 'хватит' in exersize or 'прекрати' in exersize :
        talk('Да, конечно')
        sys.exit()
    elif 'погода' in exersize:
        talk('Скажите город, в котором хотите узнать погоду: ')
        r = sr.Recognizer()
        with sr.Microphone() as source1:
            audio1 = r.listen(source1)
            nameOFcity = r.recognize_google(audio1, language="ru-Ru").lower()
            observation = owm.weather_at_place(nameOFcity)
            w = observation.get_weather()
            temp = w.get_temperature('celsius')["temp"]
        talk(' В городе ' + str(nameOFcity) + ' сейчас ' + w.get_detailed_status())
        talk('Температура в районе ' + str(temp) + 'градусов')
    elif 'что ты умеешь' in exersize or 'твои умения' in exersize or 'твои таланты' in exersize:
    	talk('Я умею говорить время, открывать сайты, знаю погоду и пока я на стадии разработки. ха-ха')
    elif 'анекдот' in exersize or 'расскажи анекдот' in exersize or 'расскажи шутку' in exersize or 'шутка' in exersize:
        if a == 1:
            talk('Страшные времена. Людям приходится мыть руки, готовить дома еду и общаться со своими детьми. Так может дойти и до чтения книг. ХА ХА')
   	    
        elif a == 2:
            talk('Сотрудница отдела продаж, специалист по сервису и их начальник идут обедать и находят старую масляную лампу.') 
            talk('Они трут лампу, и Джин появляетсaneя в облаке дыма. Джин говорит: — Обычно я выполняю три желания, поэтому каждый из Вас может загадать по одному.')
            talk('— Чур, я первая!, — говорит сотрудница отдела продаж. Я хочу быть сейчас на Багамах, мчаться без забот на скутере по волнам. Пуфф! И она растворяется в воздухе. — Я следующий!, — говорит спец по сервису.') 
            talk('Я хочу на Гавайи, расслабляться на пляже с личной массажисткой и бесконечным запасом Пина-Колады. Пуфф! Исчезает. — OK, твоя очередь!, — говорит Джин менеджеру. ')
            talk('Тогда менеджер говорит: — Я хочу, чтобы эти двое были в офисе после обеда. Мораль: Всегда дай начальнику высказаться первым. ха-ха')
   	    
        elif a == 3:
            talk('Стоит мужик у Кремля с плакатом "Воров на нары". Его задерживает полиция за оскорбление власти. Мужик: — Да я даже про власть ничего не сказал! Полицейские: — А то мы не знаем, кто тут воры...')

    elif 'найди' in exersize or 'узнай' in exersize:
    	talk('Что вас интересует?')
    	r = sr.Recognizer()
    	with sr.Microphone() as source2:
    		audio2 = r.listen(source2)
    		nameOFsearch = r.recognize_google(audio2, language="ru-Ru").lower()
    	webbrowser.open_new_tab('https://yandex.ru/search/?text='+nameOFsearch)
    elif 'переведи' in exersize or 'перевод' in exersize or 'переводчик' in exersize:
    	talk('На какой язык вы хотите перевести слово?')
    	r = sr.Recognizer()
    	with sr.Microphone() as source3:
    		audio3 = r.listen(source3)
    		language= r.recognize_google(audio3, language="ru-Ru").lower()
    		if 'французкий' in language or 'французкий' in language:
    			nameOFlanguage = 'fr'
    		elif 'русский' in language or 'руский' in language:
    			nameOFlanguage = 'ru'
    		elif 'арабский' in language:
    			nameOFlanguage = 'ar'
    		elif 'испанский' in language:
    			nameOFlanguage = 'es'
    		elif 'индонезиский' in language or 'индонезийский' in language:
    			nameOFlanguage = 'id'
    		elif 'португальский' in language:
    			nameOFlanguage = 'pt'
    		elif 'бенгальский' in language:
    			nameOFlanguage = 'bn'
    		elif 'хинди' in language or 'синди' in language or 'бенди' in language:
    			nameOFlanguage = 'hi'
    		elif 'английский' in language:
    			nameOFlanguage = 'en'
    		elif 'китайский' in language:
    			nameOFlanguage = 'zh'
    		elif 'японский' in language:
    			nameOFlanguage = 'ja'
    		elif 'турецкий' in language:
    			nameOFlanguage = 'tr'
    		elif 'немецкий' in language:
    			nameOFlanguage = 'de'
    	try:
    		language = r.recognize_google(audio3, language="ru-Ru").lower()
    		print('Вы сказали : ' + language)
    	except sr.UnknownValueError:
    		talk('Я вас не поняла , повторите пожалуйста ')
    		language = commands()
    		return language
    	talk('Какое слово вы хотите перевести ?')
    	r = sr.Recognizer()
    	with sr.Microphone() as source4:
    		audio4 = r.listen(source4)
    		nameOFsearch = r.recognize_google(audio4, language="ru-Ru").lower()
    	try:
    		nameOFsearch = r.recognize_google(audio4, language="ru-Ru").lower()
    		print('Вы сказали : ' + nameOFsearch)
    	except sr.UnknownValueError:
    		talk('Я вас не поняла , повторите пожалуйста ')
    		nameOFsearch = commands()
    		return nameOFsearch
    	talk(tr.translate(nameOFsearch, nameOFlanguage))

while True:
    makeSomeThing(commands())
