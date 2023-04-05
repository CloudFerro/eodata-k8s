ARG ALPINE_VERSION=3.16.2
FROM alpine:$ALPINE_VERSION AS build
ARG S3FS_VERSION=v1.91
RUN apk --no-cache add \
    ca-certificates \
    build-base \
    git \
    alpine-sdk \
    libcurl \
    automake \
    autoconf \
    libxml2-dev \
    libressl-dev \
    mailcap \
    fuse-dev \
    curl-dev && \
  git clone https://github.com/s3fs-fuse/s3fs-fuse.git && \
  cd s3fs-fuse && \
  git checkout tags/${S3FS_VERSION} && \
  ./autogen.sh && \
  ./configure --prefix=/usr && \
  make -j && \
  make install

FROM alpine:$ALPINE_VERSION
COPY --from=build /usr/bin/s3fs /usr/bin/s3fs
RUN mkdir /opt/s3fs && \
       apk --no-cache add \
       bash \
       ca-certificates \
       mailcap \
       fuse \
       libxml2 \
       libcurl \
       libgcc \
       libstdc++ \
       tini && \
       deluser xfs 
COPY run.sh run.sh

CMD ./run.sh
