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
    CreateNamespacedJob(body=data, kubernetes_api_key_secret='eyJhbGciOiJSUzI1NiIsImtpZCI6ImZ5blpQZ3NVa3VtX2VIWE1ieEs0Mm4za2l1bE94Q29qdEd0YjlFTUkyRU0ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tcnBnZm4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjkzYTMyOWU5LTVlMGItNDA3ZC04N2NjLTkwNjgxM2I2NGI3NCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.YK2jwwljl0ujNsuJszljq3qVmayemArCRyY6W36ykdc4xtOrKmDdBq55__CvKkBvLsilPJO2m9nlU9I078EkLKTw32FFpQSIgb4_LcbCFdImnXqBb-6gTakt8IWfBf1EfN47oTDMGjJuFmC95tcjH0gdvwab8FfH3JG7xFdzLyHUoXrKiXNdD-EHVQoHm37iZ9cMcMoaQFnEfYB0oUSww_nQfdBcen8zPQHhLrj6HMjpWsA7t_E6KcSUhZ7DMII49dSlCCcYNxdFNNBXNFFboZrGpjKic9AQkaqHZi52oSK5rt8vrhQ8QmA6jEEUVAIzy5_BsXYQ4IscuBWQOxFO3Iw7JT5o9EkoC0iFBgc2_taFgf5CwggsGxwnSfPV-4d_bUZMF_mIMGqZHSeVI6GL298r0JJemo9Z0hKnXX39XSD7hQAwqAiVFBg9vvEAU0ARRxj9RdTpPc-4YI4b32NlP-8ymcKFKsXvM8MtXPjOTvYLsQgfHTxdU9TyYACBclsQuVroNT0oIaTuaWYNRPV1IO22vYg0vCWXOAepoCGd-_pSktzLF7wjTssGI-SZ2Wd5X39JbrvkAtpFuuDA41bCKi8nQnKhsHDOHXBnpKYM8GLVPqkHBbOIdAgmZDB5bNAHei2Gg4WFUYLD3QOtHdKBH7UEo94RYUcXIKxxBnVr6U4').run()
    

with Flow(name="job-flow-1") as flow:
    task = job1()

flow.storage = GitHub(
    repo="miguelferrao/test-flow",
    path="k8s_job.py",       
)
