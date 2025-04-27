FROM python:3.9

WORKDIR /trading

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "trading.main:app", "--host", "0.0.0.0", "--port", "8001"]