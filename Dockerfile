FROM python:3.10

WORKDIR /app

COPY req.txt requirements.txt

COPY example.env .env

RUN pip install --upgrade pip

RUN pip install --no-cache --user -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-m", "flask", "run" , "--host=0.0.0.0"]
