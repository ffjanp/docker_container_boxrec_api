FROM python:3.5.3

WORKDIR /app/

COPY requirements.txt /app/
COPY test.html /app/templates/test.html
COPY boxer_features.p /app/
COPY boxer_name_id.p /app/
RUN pip install -r ./requirements.txt

COPY app.py __init__.py /app/

# ENTRYPOINT /bin/bash
EXPOSE 5000

ENTRYPOINT python ./app.py
