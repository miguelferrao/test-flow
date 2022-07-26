from prefect import task, Flow
from prefect.tasks.kubernetes.job import CreateNamespacedJob
import yaml
from yaml import SafeLoader
from prefect.run_configs import KubernetesRun
from prefect.storage import GitHub
import requests


@task
def job1():
    url = 'https://raw.githubusercontent.com/miguelferrao/test-flow/0908802d9ac94a7ceb2a53c0ac344f9e288fffa1/flows/job.yaml'
    download = requests.get(url).content
    data = yaml.load(download, Loader=SafeLoader)
    CreateNamespacedJob(body=data, kubernetes_api_key_secret='89b6ae1c-c52c-4683-a67b-86e35da26e29').run()
    

with Flow(name="job-flow-1") as flow:
    task = job1()

flow.storage = GitHub(
    repo="miguelferrao/test-flow",
    path="k8s_job.py",       
)

flow.run()
