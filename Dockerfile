# Dockerfile has three Arguments: base, tag, branch
# base - base image (default: python)
# tag - tag for base mage (default: stable-slim)
# branch - user repository branch to clone (default: python)
#
# To build the image:
# $ docker build -t <dockerhub_user>/<dockerhub_repo> --build-arg arg=value .
# or using default args:
# $ docker build -t <dockerhub_user>/<dockerhub_repo> .

# set the python version (e.g. 2, 3, 3.8, 3.7 : for python)
ARG version=3

## Build stage 0: Compule using a base python image
FROM python:${version}

# Set environments
ENV LANG C.UTF-8

# Set working directory
RUN mkdir /buildroot
WORKDIR /buildroot

# Copy our python application
COPY . .

# And build the release
RUN python3 setup.py sdist


## Build stage 1: Clean installation in slim
FROM python:${version}-slim
LABEL maintainer='B.Esteban (KIT)'

# Which user and group to use 
ARG user=application
ARG group=standard

# Set environments
ENV LANG C.UTF-8
ENV APP /app

# Install system updates and tools
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Install system updates and tools
    ca-certificates \
    gcc g++ && \
    # Clean up & back to dialog front end
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Set workdirectory
RUN mkdir $APP
WORKDIR $APP

# Copy the released application
COPY --from=0 /buildroot/dist dist

# Install python application
RUN pip install --upgrade pip && \ 
    pip install --no-cache-dir ./dist/*.tar.gz && \
    # Clean up
    rm -rf /root/.cache/pip/* && \
    rm -rf /tmp/*

# Change user context and drop root privileges
RUN groupadd -r ${group} && \
    useradd --no-log-init -r -d /app -g ${group} ${user} && \
    chown -R ${user} . 
USER ${user}

# Start default script
ENTRYPOINT [ "cli_script" ]
CMD [ "--verbosity ERROR" ]

