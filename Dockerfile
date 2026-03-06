FROM python:3.12-alpine3.19
WORKDIR /app
LABEL authors="Sergeial1972-user"

COPY requirements.txt ./

RUN python3 -m venv --without-pip venv
RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["top", "-b"]