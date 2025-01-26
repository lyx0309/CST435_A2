#!/bin/bash
#
microk8s helm3 repo add pfisterer-hadoop https://pfisterer.github.io/apache-hadoop-helm/
microk8s helm3 install hadoop pfisterer-hadoop/hadoop