FROM python:3.10 AS base
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 80
# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=80", "--browser.gatherUsageStats", "false"]
