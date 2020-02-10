FROM debian:buster

# Install git, supervisor, VNC, & X11 packages
RUN set -ex; \
    apt-get update; \
    apt-get install -y \
    bash \
    fluxbox \
    git \
    net-tools \
    novnc \
    supervisor \
    x11vnc \
    xterm \
    xvfb

# Setup demo environment variables
ENV HOME=/root \
    DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    DISPLAY=:0.0 \
    DISPLAY_WIDTH=1900 \
    DISPLAY_HEIGHT=920

RUN echo '[supervisord]\n\
nodaemon=true\n\
\n\
[program:fluxbox]\n\
command=fluxbox\n\
autorestart=true\n\
\n\
[program:websockify]\n\
command=websockify --web /usr/share/novnc 8080 localhost:5900\n\
autorestart=true\n\
\n\
[program:x11vnc]\n\
command=x11vnc -forever -shared\n\
autorestart=true\n\
\n\
[program:xterm]\n\
command=xterm\n\
autorestart=true\n\
\n\
[program:xvfb]\n\
command=Xvfb :0 -screen 0 "%(ENV_DISPLAY_WIDTH)s"x"%(ENV_DISPLAY_HEIGHT)s"x24 -listen tcp -ac\n\
autorestart=true' > supervisord.conf

RUN apt-get install python3 \
                    python3-pip \
                    python3-dev \
                    chromium -y

RUN mkdir code
COPY . /code
WORKDIR /code
RUN pip3 install -e .
CMD ["supervisord", "-c", "/supervisord.conf"]

EXPOSE 8080