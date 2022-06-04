FROM python:3.9.13-slim
RUN mkdir /pytest-api-booking/
ADD ..  /pytest-api-booking/
WORKDIR /pytest-api-booking/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY /entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]