FROM python:3.8-buster as buildsys
WORKDIR /usr/src/pdfexport
RUN apt-get update && \
  apt-get install -y wkhtmltopdf cron psmisc

FROM buildsys as pandassys
RUN pip install numpy==1.16.4 && \
  pip install pandas==0.23.4

FROM pandassys
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
  mkdir /var/tmp/pdfcache

COPY . .
RUN chmod +x startup.sh
CMD ["./startup.sh"]

EXPOSE 7002
