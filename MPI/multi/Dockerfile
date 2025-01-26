# base image
FROM ubuntu:20.04

# for non-interactive frontend for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# install necessary packages
RUN apt-get update && apt-get install -y \
    tzdata openmpi-bin openmpi-common openssh-server build-essential python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# set the timezone to UTC
ENV TZ=Etc/UTC
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

# install mpi4py
RUN pip3 install mpi4py

# create a user for running the application
RUN useradd -m mpiuser
USER mpiuser
WORKDIR /home/mpiuser

# copy Python MPI program and input into the image
COPY --chown=mpiuser:mpiuser mpi_avg_view.py input.csv .

# default command to keep the container alive
CMD ["/bin/bash"]
