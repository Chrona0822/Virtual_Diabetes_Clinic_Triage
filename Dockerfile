FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/

RUN python src/train.py

EXPOSE 8000

CMD ["python", "src/api.py"]