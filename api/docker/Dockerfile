# Dockerfile
FROM python:3.10-slim

# Installiere Abhängigkeiten
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest der Anwendung
COPY . /app

# Starte die Anwendung mit uvicorn
CMD ["uvicorn", "main_prod:app", "--host", "0.0.0.0", "--port", "8000"]