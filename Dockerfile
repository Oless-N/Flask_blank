FROM python:3.7.4-alpine3.9

ARG develop=1
ARG build_version=0.1
ENV DEVELOP=1 \
    BUILD_VERSION=0.1 \
    USER=transaction_limiter \
    UID=900 \
    GID=901

WORKDIR /service

RUN addgroup --gid "$GID" "$USER" \
    && adduser -D -H -u "$UID" "$USER" -G "$USER" \
    && apk add --virtual build-deps gcc python3-dev musl-dev build-base linux-headers \
    && pip3 install --upgrade pip setuptools \
    && chown -R $USER:$USER /service \
    && apk --no-cache add curl


COPY requirements requirements
COPY transaction_limiter transaction_limiter
COPY tests tests
COPY configs configs

RUN pip install -r requirements/requirements.txt

RUN chown -R "$USER":"$USER" /service

USER "$USER"

EXPOSE 5050

ENTRYPOINT ["python3"]
CMD ["transaction_limiter/main.py"]