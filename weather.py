import pyowm

owm = pyowm.OWM('362e29adf58f81ebe0d5078fc2d3ab1e')
mrg = owm.weather_manager()

status = ''
temp = ''
feelstemp = ''
advice = 'Підказка: '

place = input("Ввдеіть місто: ") 

observation = mrg.weather_at_place(place)
w = observation.weather

if w.detailed_status == 'overcast clouds' :
    status += 'помірно хмарно'
elif w.detailed_status == 'clear sky' :
    status += 'чисте небо'
elif w.detailed_status == 'heavy intensity rainy' :
    status += 'сильний дощ'
elif w.detailed_status == 'light rain' :
    status += 'легкий дощ'
elif w.detailed_status == 'moderate rainy':
    status += 'помірний дощ'
elif w.detailed_status == 'few clouds':
    status += 'ледве хмарно'
elif w.detailed_status == 'broken clouds':
    status += 'місцями хмарно'
else :
    status += w.detailed_status + 'error'
    
temp1 = w.temperature('celsius')
temp = w.temperature('celsius')['temp']
feelstemp = w.temperature('celsius')['feels_like']

if feelstemp >= 20 and feelstemp < 30 :
    advice += 'Вдівайся легко на дворі тепло'
elif feelstemp >= 30 :
    advice += 'Але там парілка'
elif feelstemp < 20 and feelstemp > 10 :
    advice += 'Вдівайся тепло, на дворі прохолодно'
elif feelstemp < 20 :
    advice += 'На дворі дуже холодно!'
print ("В місті " + place + " зараз " + status + " " + str(temp) + "C°, "
       + "відчувається як: " + str(feelstemp) + "C°")
print(advice)

input()

