FROM python:slim-bullseye

RUN mkdir /opt/app

RUN chmod 777 /opt/app

WORKDIR /opt/app

COPY ./requirements.txt ./requirements.txt

COPY ./app.py ./app.py

RUN pip install -r requirements.txt

EXPOSE 4141

CMD [ "uvicorn", "app:app","--host","0.0.0.0", "--port", "4141"]