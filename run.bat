@echo off
call venv\scripts\activate
pytest -v -s --html .reports\test_report.html --browser chrome
pause
