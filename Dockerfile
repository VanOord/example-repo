# Start with docker image from anaconda
FROM continuumio/miniconda3:4.6.14
ARG GITHUB_TOKEN

ADD . /example-repo
WORKDIR /example-repo

RUN conda install numpy pandas nomkl pyproj

RUN pip install --upgrade pip && \
    pip install -r test-requirements.txt && \
    pip install -e .

EXPOSE 8888