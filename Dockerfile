FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/DazRepo/Uro-bot /home/uro-bot/ \
    && chmod 777 /home/uro-bot \
    && mkdir /home/uro-bot/bin/

WORKDIR /home/uro-bot/

CMD [ "bash", "start" ]
