# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

### Установка
- Установите необходимые библиотеки.
```python
pip install -r requirements.txt
```
- Подготовьте Excel файл в таком формате:

|**Категория**|**Название**       |**Сорт**       |**Цена**|**Картинка**            |**Акция**           |
|-------------|-------------------|---------------|--------|------------------------|--------------------|
|Белые вина   |Белая леди         |Дамский пальчик|399     |belaya_ledi.png         |Выгодное предложение|
|Напитки      |Коньяк классический|               |350     |konyak_klassicheskyi.png|                    |
|Красные вина |Черный лекарь      |Качич          |399     |chernyi_lekar.png       |                    |
  
### Запуск
- Положите вашь Excel файл (wine.xlsx) в корень папки с проектом.
- Запустите сайт командой:
```python
python main.py -f wine.xlsx
```
- Перейдите на сайт по адресу:
```python
http://127.0.0.1:8000
```
### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
