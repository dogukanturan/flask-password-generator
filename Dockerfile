FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*
CMD ["python","app.py"]
EXPOSE 80
