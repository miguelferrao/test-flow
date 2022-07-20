from prefect import task, Flow
from prefect.tasks.kubernetes.job import CreateNamespacedJob
import yaml
from yaml import SafeLoader
from prefect.run_configs import KubernetesRun
from prefect.storage import Docker


@task
def job1():
    with open('job.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
        CreateNamespacedJob(body=data, kubernetes_api_key_secret=None).run()
    

with Flow(name="job-flow-1", run_config=KubernetesRun(), storage=Docker(registry_url="my-registry.io", image_name="my_flow")) as flow:
    task = job1()

flow.register("tester")
