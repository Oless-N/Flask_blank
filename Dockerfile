FROM python:3.7.4-alpine3.9

ARG develop=1
ARG build_version=0.001
ENV DEVELOP=1 \
    BUILD_VERSION=0.001 \
    USER=workchain \
    UID=900 \
    GID=901

WORKDIR /service

RUN addgroup --gid "$GID" "$USER" \
    && adduser -D -H -u "$UID" "$USER" -G "$USER" \
    && apk add --virtual build-deps gcc python3-dev musl-dev build-base linux-headers \
    && pip install --upgrade pip setuptools \
    && chown -R $USER:$USER /service \
    && apk --no-cache add curl mc

COPY transaction_limiter requirements

RUN pip install -r requirements/requirements.txt

COPY transaction_limiter workchain
COPY tests tests
COPY configs /etc/workchain

COPY shell shell
RUN chown -R "$USER":"$USER" /service

USER "$USER"

EXPOSE 7575

CMD python3 main.py