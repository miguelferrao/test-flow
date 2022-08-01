from prefect import task, Flow
from prefect.storage import GitHub

@task
def get_data():
    return [1, 2, 3, 4, 5]

@task
def print_data(data):
    print(data)

with Flow("example") as flow:
    data = get_data()
    print_data(data)

flow.storage = GitHub(
    repo="miguelferrao/test-flow",                            # name of repo
    path="flows/my_flow.py"                 
)