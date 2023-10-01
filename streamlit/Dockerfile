FROM python:3.10 AS base
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501", "--browser.gatherUsageStats", "false"]
