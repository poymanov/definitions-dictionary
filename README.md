# Поиск определений в словаре

## Установка и запуска

- Разместить файлы приложения в любой директории
- Выполнить файл `main.py`:

```
python3 main.py
```

## Описание

Приложение требует вести простое слово на английском языке в любом формате (*river*, *River*, *RiVeR*), 
находит и отображает одно или несколько совпадений.

Слова и их определения находятся в `data.json`

Если слово введено со ошибкой (*riverr*, *rriver*), то приложение отображает список слов,
которые могли иметься ввиду и предлагает осуществить повторный ввод корректного слова для повторного поиска в словаре.