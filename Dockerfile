FROM debian:jessie

RUN apt-get -yqq update && \
    apt-get -yqq install curl unzip && \
    apt-get -yqq install python3 && \
    apt-get -yqq install git

# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*


RUN mkdir -p /usr/src/app

RUN adduser virginpulse \
    && chown -R virginpulse:virginpulse /usr/src/app

WORKDIR /usr/src/app
RUN git clone https://github.com/mtdoyle/virginpulsedailies.git
WORKDIR /usr/src/app/virginpulsedailies

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

RUN pip3 install -r requirements.txt

ENV USERNAME=mike.doyle@thomsonreuters.com \
    PASSWORD=*l1%L2Cyat91O$gZ \
    CHROMEDRIVERPATH=/usr/local/bin/chromedriver


USER virginpulse

CMD python3 /usr/src/app/virginpulsedailies/src/virginpulsedailies.py