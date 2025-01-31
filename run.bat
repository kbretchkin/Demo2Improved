@echo off
call venv\scripts\activate
pytest -s -v --html .reports\test_report.html --browser chrome
pause