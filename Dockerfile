FROM ubuntu:jammy-20231004

ENV USER=root DEBIAN_FRONTEND=noninteractive
VOLUME ["/var/cache/apt/archives"]
RUN touch /.dockerenv

RUN apt-get update \
    && apt-get install --yes \
        git \
        language-pack-en \
        language-pack-fi \
        locales \
        locales-all \
        netcat \
        sudo \
        vim \
        zsh \
    && echo '%sudo ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/sudo_nopasswd \
    && apt-get install --yes --no-install-recommends \
        gdal-bin \
        python3 \
        python3-cryptography \
        python3-lxml \
        python3-memcache \
        python3-ndg-httpsclient \
        python3-paste \
        python3-pil \
        python3-pip \
        python3-psycopg2 \
        python3-pyasn1 \
        python3-pyproj \
        python3-rcssmin \
        python3-requests \
        python3-six \
        python3-socks \
        python3-urllib3 \
        python3-venv \
        python3-wheel

RUN dpkg-reconfigure locales
RUN useradd -m -u 1000 bew
RUN usermod -aG sudo -s /usr/bin/zsh bew
COPY zshrc /home/bew/.zshrc
COPY bashrc /home/bew/.bashrc
RUN chown -R bew:bew /home/bew

USER bew
ENV USER=bew
ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_CTYPE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
WORKDIR /home/bew/bew

COPY --chown=bew:bew . /home/bew/bew/

RUN python3.10 -m venv --system-site-packages /home/bew/.venv
RUN /home/bew/.venv/bin/pip3 install -r /home/bew/bew/requirements.txt
RUN /home/bew/.venv/bin/pip3 install -r /home/bew/bew/requirements-dev.txt
RUN /home/bew/.venv/bin/pip3 install -r /home/bew/bew/requirements-test.txt
RUN /home/bew/.venv/bin/pip3 install -r /home/bew/bew/requirements-style.txt

CMD /bin/zsh
