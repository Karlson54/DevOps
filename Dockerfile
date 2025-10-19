FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["tail", "-f", "/dev/null"]