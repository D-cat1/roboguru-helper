FROM alpine:latest
FROM alfg/ffmpeg:latest

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
    aria2 \
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
    tesseract-ocr-data-ind \
    figlet
    
RUN apk --no-cache add ca-certificates wget  && \
        wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
        wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk && \
        apk add glibc-2.29-r0.apk

RUN cp /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN git clone https://ba69af3b1eded5e362869c25f778d0ec9ae2873d@github.com/cutiecat-chan/waUbot /root/waUbot
RUN mkdir /root/waUbot/bin/
WORKDIR /root/waUbot/

ENV TZ=Asia/Jakarta

RUN npm install

CMD ["npm", "start"]
