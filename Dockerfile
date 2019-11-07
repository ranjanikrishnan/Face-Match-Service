FROM python:3.7
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pwd
RUN ls
CMD python ./src/app.py
