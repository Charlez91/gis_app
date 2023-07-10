FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Setup working directory
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt update && apt install -y lsb-release && apt clean all

# Setup Postgres
RUN wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg-testing main 13" | tee  /etc/apt/sources.list.d/pgdg-testing.list
RUN apt-get -y update 
RUN apt-get -y upgrade
RUN apt -y --fix-missing install postgresql-client-13


# Setup Postgis
RUN apt -y install postgresql-10-postgis-scripts
RUN apt-get -y install postgresql-contrib


# Setup GDAL
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin python3-gdal

COPY . /code/
