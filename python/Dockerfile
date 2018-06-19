FROM python:3-onbuild
COPY . /usr/src/app
CMD  ["sh", "-c", "python db_create.py && python api.py"]

