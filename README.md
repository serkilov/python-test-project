1. Пакеты для venv в ./requirements.txt
2. Инициализация БД
   * `python ./scripts/initiate_db.py`
3. Запуск тестов
   * `pytest --alluredir=./tests/reports -s`
4. Запись в БД
   * `python ./scripts/record_results.py`
