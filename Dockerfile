FROM python:3.5.3

WORKDIR /app/

COPY requirements.txt /app/
COPY ./templates/index.html /app/templates/
COPY boxer_features.p /app/
COPY boxer_name_id.p /app/
COPY ./website/images/background.jpg ./templates/images/
COPY ./website/images/logo.png ./templates/images/
RUN pip install -r ./requirements.txt

COPY app.py __init__.py /app/

# ENTRYPOINT /bin/bash
EXPOSE 5000

ENTRYPOINT python ./app.py
