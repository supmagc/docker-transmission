FROM linuxserver/transmission
MAINTAINER supmagc

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="supmagc Transmission version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# install packages
RUN \
 apk add --no-cache \
    curl \
    p7zip \
    python2 \
	py-pip \
    unrar \
    wget \
    git \
    unzip \
    tar \
    ffmpeg && \
 pip install transmissionrpc && \
 apk del py-pip

# add local files
COPY root/ /

# ports and volumes
VOLUME /nzbtomedia
