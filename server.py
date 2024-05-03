from kubernetes import client, config,utils
from flask import Flask,request
from os import path
import yaml, random, string, json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()
app = Flask(__name__)
# app.run(debug = True)

class Pod:
  def __init__(self, name, ip,node,namespace,status):
    self.node = node
    self.ip = ip
    self.namespace = namespace
    self.name = name
    self.status = status

@app.route('/config', methods=['GET'])
def get_config():
    pods = []
    pod_list = v1.list_namespaced_pod("free-service")
    # your code here
    for pod in pod_list.items:
        podObject = Pod(pod.metadata.name,pod.status.pod_ip,pod.spec.node_name,pod.metadata.namespace,pod.status.phase)
        pods.append(podObject.__dict__)
    pod_list = v1.list_namespaced_pod("default")
    for pod in pod_list.items:
        podObject = Pod(pod.metadata.name,pod.status.pod_ip,pod.spec.node_name,pod.metadata.namespace,pod.status.phase)
        pods.append(podObject.__dict__)
    pod_list = v1.list_namespaced_pod("kube-system")
    for pod in pod_list.items:
        podObject = Pod(pod.metadata.name,pod.status.pod_ip,pod.spec.node_name,pod.metadata.namespace,pod.status.phase)
        pods.append(podObject.__dict__)
    output = {"pods": pods}
    output = json.dumps(output)

    return output

@app.route('/img-classification/free',methods=['POST'])
def post_free():
    # your code here
    k8s_client = client.ApiClient()
    yaml_file = './free_job.yaml'
    # your code here
    utils.create_from_yaml(k8s_client, yaml_file)
    return "success"


@app.route('/img-classification/premium', methods=['POST'])
def post_premium():
    # your code here
    k8s_client = client.ApiClient()
    yaml_file = './premium_job.yaml'
    # your code here
    utils.create_from_yaml(k8s_client, yaml_file)
    return "success"

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
