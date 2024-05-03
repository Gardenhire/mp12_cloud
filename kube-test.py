from kubernetes import client, config,utils
import json
from os import path

class Pod:
  def __init__(self, name, ip,node,namespace,status):
    self.name = name
    self.ip = ip
    self.node = node
    self.namespace = namespace
    self.status = status

config.load_kube_config()
v1 = client.CoreV1Api()
k8s_client = client.ApiClient()
yaml_file = './free_job.yaml'
    # your code here
utils.create_from_yaml(k8s_client, yaml_file)

pod_list = v1.list_namespaced_pod("free-service")

for pod in pod_list.items:
    podObject = Pod(pod.metadata.name,pod.status.pod_ip,pod.spec.node_name,pod.metadata.namespace,pod.status.phase)
    print(podObject.__dict__)
#output = {"pods": pods}
#output = json.dumps(output)