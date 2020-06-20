# Base Image
FROM python:3.8-buster

# create and set working directory
RUN mkdir /app
RUN mkdir /environment
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install project dependencies
RUN python3 -m venv /environment
RUN . /environment/bin/activate
RUN pip install -r requirements.txt