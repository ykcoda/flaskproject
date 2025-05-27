FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 5000

ENV FLASK_APP=app.py 
ENV FLASK_RUN_HOST=0.0.0.0 

#run flask applicationss
CMD ["flask", "run"]