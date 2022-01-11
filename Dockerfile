FROM alpine:3.15
RUN  apk add --update --no-cache python3 && apk add py-pip && pip install flask
ADD ./api.py /
ENTRYPOINT ["python3", "./api.py"]
