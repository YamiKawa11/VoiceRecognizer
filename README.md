Проект написан на PyQt5 и использет следующие библиотеки:
pip install PyQt5
pip install pandas
pip install pyaudio
pip install librosa
pip install matplotlib
pip install pydub


StartUp:
Скачайте python 3.11.X

Установите библиотеки указанные выше и запустите main.py

Если возникла вот такая ошибка:
Qt.qpa.plugin: Could not find the Qt platform plugin «windows» in «»?

![image](https://github.com/YamiKawa11/VoiceRecognizer/assets/139690866/63efa874-8aa3-4043-8c6a-0474507b21bb)
https://qna.habr.com/q/920179
Следуйте этой инструкции


Как пользоваться программой:

![image](https://github.com/YamiKawa11/VoiceRecognizer/assets/139690866/8927d452-76a9-4c39-94cf-ae938e36ccac)
Регистрируем админа и запоминаем данные.

![image](https://github.com/YamiKawa11/VoiceRecognizer/assets/139690866/5a37de1e-54f9-4d76-b958-1915da79d203)
Для распознавания нужно как минимум 2 пользовтеля(Алгоритм классификации)
Регестрируем их, перезагружаем программу и пробуем войти.


Технологии:
Для распознавания использовал SVC из sklearn
За признаки взял Мел кепстральные коофиценты(в интернете найдёте : ) )
Извлечение признаков происходит в файле src/Static.py, если интересно найдёте там всё


