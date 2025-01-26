#!/bin/bash
#
microk8s kubectl cp  ./code_input hadoop-hadoop-yarn-nm-0:/opt/hadoop-3.3.2/hadoop-test
microk8s kubectl exec -it hadoop-hadoop-yarn-nm-0 -- bash