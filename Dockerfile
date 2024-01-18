FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY . .
COPY .streamlit/ ./

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

EXPOSE 8010

ENTRYPOINT ["streamlit", "run", "chatbot.py", "--server.port=8010", "--server.address=0.0.0.0"]
