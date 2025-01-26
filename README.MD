# Performance Analysis of Hadoop Map Reduce and MPI in Single and Multi Nodes Environments

## Overview

The increasing volume of big data generated in various domains, such as social media, streaming platforms, and e-commerce, presents significant challenges in processing and analyzing such data efficiently. High availability and scalability are critical to ensuring reliable performance when handling large datasets. Kubernetes, as a container orchestration platform, offers the ability to form a high-availability cluster that can distribute workloads across multiple nodes, ensuring fault tolerance and optimized resource utilization.

This project aims to explore the performance of Hadoop MapReduce and MPI (Message Passing Interface) when implemented within a MicroK8s Kubernetes cluster, with a focus on processing YouTube video data to compute the top five countries with the highest average number of views on YouTube videos.

### Objectives

- Implement Hadoop MapReduce and MPI in a MicroK8s Kubernetes cluster.
- Process YouTube video data to calculate the top five countries with the highest average views.
- Compare the performance of a single-node Kubernetes cluster against a multi-node Kubernetes cluster.
- Evaluate the efficiency of distributed systems in a containerized environment for big data analysis.

## Input File

The input file for this project is a **chunk** from the original dataset. It has been preprocessed to focus on key columns (7th and 8th) for analysis.
