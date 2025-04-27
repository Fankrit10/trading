@echo off
SETLOCAL

REM Activate virtual environment
call venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Run tests and coverage
coverage run -m pytest
coverage report -m

REM Run linting
flake8 .
pylint trading\.

REM Run security checks
bandit -r trading\ -x trading\tests,trading\venv,trading\__pycache__,trading\.pytest_cache,trading\fakes


REM Docker commands
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d

REM Bring down docker-compose
docker-compose -f docker-compose.yml down

REM Test deploy
REM Start uvicorn in the background using start
start /B uvicorn trading.main:app --host 0.0.0.0 --port 8001

REM Wait a little to ensure the server starts up
timeout /t 5 /nobreak >nul

REM Run the newman tests
newman run collection.json --environment LOCAL.postman_environment.json

REM Stop the uvicorn process
REM Find the PID of the uvicorn process and kill it
for /f "tokens=2" %%a in ('tasklist ^| findstr uvicorn') do (
    taskkill /F /PID %%a
)

ENDLOCAL
pause