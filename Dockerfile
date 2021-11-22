FROM alpine:latest
FROM inetsoftware/alpine-tesseract:latest


RUN apk add --update --no-cache \
    npm \
    git \
    python3 \
    build-base \
    python3-dev \
    py3-configobj \
    py3-pip \
    py3-setuptools \
    graphicsmagick \
    g++ \
    curl \
    libpng \
    libpng-dev \
    jpeg-dev \
    pango-dev \
    cairo-dev \
    giflib-dev \
    pkgconfig \
    make \
    neofetch \
    tzdata \
    libwebp \
    speedtest-cli \
    tesseract-ocr \
    figlet
    
RUN apk --no-cache add ca-certificates wget  && \
        wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
        wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk && \
        apk add glibc-2.29-r0.apk

RUN cp /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN git clone git@github.com:D-cat1/roboguru-helper.git /root/helper
WORKDIR /root/helper/

ENV TZ=Asia/Jakarta

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]
