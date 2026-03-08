FROM python:3.12-alpine3.19
WORKDIR /app
LABEL authors="Sergeial1972-user"

COPY requirements.txt ./
COPY main.py ./

RUN python3 -m venv venv
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

#ENV vars
#transport [streamable-http, ]
ENV TRANSPORT=streamable-http

ENV HOST=0.0.0.0
ENV PORT=8080

ENV TIMEOUT=10

ENTRYPOINT ["./venv/bin/python", "main.py"]