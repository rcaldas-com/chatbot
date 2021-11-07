FROM    python:latest
LABEL   maintainer="RCaldas <docker@rcaldas.com>"

WORKDIR /app
COPY    requirements.txt        /app/
RUN     pip install --no-cache-dir --upgrade pip && \
        pip install --no-cache-dir -r requirements.txt &&\
        apt update && apt install -y --no-install-recommends firefox-esr && apt clean
COPY    --chmod=755     geckodriver             /usr/bin/geckodriver

ENTRYPOINT  python driver.py
COPY    app /app


# RUN     curl -Ls "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=pt-BR" -o /tmp/firefox.tar.bz2 &&\
#         tar -xjf /tmp/firefox.tar.bz2 -C /usr/share/ &&\
#         rm /tmp/firefox.tar.bz2 &&\
#         ln -fs /usr/share/firefox/firefox-bin /usr/local/bin/firefox


