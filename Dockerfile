FROM    python:latest
LABEL   maintainer="RCaldas <docker@rcaldas.com>"

WORKDIR /app
COPY    requirements.txt        /app/
RUN     pip install --no-cache-dir --upgrade pip && \
        pip install --no-cache-dir -r requirements.txt &&\
        apt update && apt install -y --no-install-recommends firefox-esr && apt clean

RUN     curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | \
                grep "browser_download_url.*linux64.tar.gz\"" | cut -d '"' -f 4 | \
                wget -qi - -O /tmp/driver.tar.gz &&\
        tar -xzpf /tmp/driver.tar.gz -C /usr/bin && rm /tmp/driver.tar.gz

ENTRYPOINT  python driver.py
COPY    app /app

