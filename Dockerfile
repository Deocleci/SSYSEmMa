# start from official image
FROM python:3.6

ENV PYTHONUNBUFFERED 1

# arbitrary location choice: you can change the directory
RUN mkdir -p /syss
WORKDIR /syss

# install psycopg2 dependencies
#RUN apk update  && apk add postgresql-dev gcc python3-dev musl-dev

# copy project
COPY requirements.txt /syss/

# install denpendencies of django
RUN pip install -r requirements.txt
COPY . .
