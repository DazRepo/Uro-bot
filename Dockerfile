FROM mrismanaziz/man-userbot:buster

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

RUN git clone -b main https://github.com/DazRepo/Uro-bot /home/uro-bot/ \
    && chmod 777 /home/uro-bot \
    && mkdir /home/uro-bot/bin/

WORKDIR /home/uro-bot/

CMD [ "bash", "start" ]
