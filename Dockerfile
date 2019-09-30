FROM triblertester/ipv8-p4a:latest

VOLUME /dist
WORKDIR /home/user

#RUN  rm -rf /home/user/.local/lib/python2.7/site-packages/pythonforandroid
RUN mkdir -p /home/user/.local/lib/python2.7/site-packages
RUN if test -L /home/user/.local/lib/python2.7/site-packages/pythonforandroid; then ln -s /home/user/pythonforadnroid /home/user/.local/lib/python2.7/site-packages/pythonforandroid; fi

RUN rm -rf /home/user/ipv8-android-service && git clone -b ${branch:-master} https://github.com/Tribler/ipv8-android-service.git && cp -r ipv8-android-service/recipes/* ~/pythonforandroid/recipes

RUN virtualenv --python=python3 venv \
    && . venv/bin/activate \
    && pip3 install -e .

WORKDIR /home/user/ipv8-android-service

RUN . /home/user/venv/bin/activate

RUN . /home/user/venv/bin/activate && ./build.sh
