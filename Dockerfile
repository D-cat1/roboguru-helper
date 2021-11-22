FROM heroku/heroku:18


# Set timezone
RUN ln -fs /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN apt update && apt -y upgrade && apt install -y tzdata locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install Dependencies
RUN apt-get update \
&& apt-get install -y python3 python3-pip tesseract-ocr tesseract-ocr-eng zlib1g libjpeg-dev


#
# Clone repo and prepare working directory
#
RUN git clone https://github.com/D-cat1/roboguru-helper.git /root/helper
WORKDIR /root/helper/

ENV TZ=Asia/Jakarta

RUN pip3 install Pillow
RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]

