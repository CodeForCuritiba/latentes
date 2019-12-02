FROM joepreludian/python-pipenv

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gdal-bin libgeos-dev && apt-get clean all

WORKDIR /data

CMD ["python"]
