from prefect import task, Flow
from prefect.tasks.kubernetes.job import CreateNamespacedJob
import yaml
from yaml import SafeLoader
from prefect.run_configs import KubernetesRun
from prefect.storage import GitHub


@task
def job1():
    with open('flows/k8s_job.py') as f:
        data = yaml.load(f, Loader=SafeLoader)
        CreateNamespacedJob(body=data, kubernetes_api_key_secret=None).run()
    

with Flow(name="job-flow-1", run_config=KubernetesRun()) as flow:
    task = job1()

flow.storage = GitHub(
    repo="miguelferrao/test-flow",
    path="k8s_job.py",       
)
