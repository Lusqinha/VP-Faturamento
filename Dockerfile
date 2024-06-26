FROM python:3.11.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


RUN git clone https://github.com/Lusqinha/VP-Faturamento.git

RUN pip3 install -r VP-Faturamento/requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "VP-Faturamento/main.py", "--server.port=8501", "--server.address=0.0.0.0"]