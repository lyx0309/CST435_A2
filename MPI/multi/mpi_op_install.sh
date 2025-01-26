#!/bin/bash
#
microk8s helm3 repo add cowboysysop https://cowboysysop.github.io/charts/
microk8s helm3 install my-mpi cowboysysop/mpi-operator