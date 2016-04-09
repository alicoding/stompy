FROM python:3.5
ENV PYTHONUNBUFFERED 1
WORKDIR /app
EXPOSE 7001
COPY ./requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir --disable-pip-version-check
COPY . /app
CMD ["python", "/app/stompy/manage.py", "runserver", "0:7001"] 
