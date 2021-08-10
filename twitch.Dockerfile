FROM python:3.8

ENV PROJECT_DIR .

WORKDIR ${PROJECT_DIR}

COPY . ${PROJECT_DIR}/

RUN pip3 install -r requirements.txt

WORKDIR ${PROJECT_DIR}/src

RUN pipenv install

CMD ["python", "twitch.py"]