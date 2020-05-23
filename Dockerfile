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

# Install requirements
RUN apt-get install python3 \
    python3-tk \
    python3-pip \
    python3-dev \
    chromium -y

# Install Automagica
RUN mkdir code
COPY . /code
WORKDIR /code
RUN pip3 install -e .

# Set Automagica Wallpaper
RUN mkdir ~/.fluxbox
RUN touch ~/.fluxbox/overlay
RUN echo "background: none" >> ~/.fluxbox/overlay
RUN touch ~/.fluxbox/lastwallpaper
RUN echo "$full $full|/code/docker/wallpaper.png||:0,0" >> ~/.fluxbox/lastwallpaper

# Copy fluxbox menu file
RUN cp /code/docker/fluxbox/menu ~/.fluxbox/menu

# Run supervisord
CMD ["supervisord", "-c", "/code/docker/supervisord.conf"]

EXPOSE 8080