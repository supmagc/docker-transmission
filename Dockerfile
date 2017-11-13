FROM linuxserver/transmission
MAINTAINER supmagc

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="supmagc Transmission version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# install packages
RUN \
 apt-get update && \
 apt-get install -y \
    curl \
    p7zip \
    python \
    unrar \
    wget \
    git \
    unzip \
    tar \
    ffmpeg && \
 git clone https://github.com/clinton-hall/nzbToMedia.git /scripts && \

# cleanup
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/* && \

# pip install
  pip install transmissionrpc

# add local files
COPY root/ /

# ports and volumes
VOLUME /nzbtomedia
