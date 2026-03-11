FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY environment.yml .

RUN pip install --no-cache-dir -r requirements.txt

COPY train.py .

CMD ["python", "train.py"]