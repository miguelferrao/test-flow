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
    CreateNamespacedJob(body=data, kubernetes_api_key_secret="MIIE6TCCAtGgAwIBAgIRAMa/ANAceQ5KXqtK5VEGNxgwDQYJKoZIhvcNAQELBQAw
DTELMAkGA1UEAxMCY2EwIBcNMjIwNTE1MDUxNTA1WhgPMjA1MjA1MTUwNTI1MDVa
MA0xCzAJBgNVBAMTAmNhMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA
stX+R/BGCnJv1H2Lws1cRCBEsR06bRN0MBDCLwQHclM6w68HjB7+Dw41x28FwhKo
er0VVjYFZq+d8Dx+59jXNJKnRQM2Th2+fX/mikR09VK7tQMZtBSaCHBR29oLSuEk
r1TUnDKmRbCdoNFEky7OLpDrmM6e/CEHvuGogVh76s1UfI5TmCrn4ipHS5ENmj7O
xBskbQBfHzkg9lvMOPZf6xbsqgkB2lkxd4ovBhhnvI+BvmHdd3XKPOrbRK4OlIOm
qRQ0CwuFCKdOhj5KPv+BDzOgOFCqmtSLE2/vVZNMwO4r7Ix+94qXj5qoRVRq/ANJ
kx59k+wz+6qthzEzBOcCXUhqI20VH6TT8JCFjX/QENJuDVXa0JDya+4gKdEV+LCE
vucPVqSlVcUG+Kiy6S/4f9jufUNEkCeQP5B7ZhBVDlV6DhRmP65WzNO7WP1ZCXm0
XmLghJFAix2CEl1SZoaFI70iEbqaZi8qFBpbBRfbIV6m1ech97i6lVG2C4G9N+/e
6O4tOY2UizmhgIdOvZnyKF9EK4PRteFreKTKt62tkoJ5PFu820Oy7QoKYgX0S2xv
VCxbKXG1XIGpPupdbf7xSLZWuzmvCDvD2hr3wOIqVfuLvh5QXuc6fX4XIqmD0NmS
+Sz7G5Nx4FWZqBTl98wszgGr7NYL5VHUR3p8hHOpH40CAwEAAaNCMEAwDgYDVR0P
AQH/BAQDAgKkMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFOLYhKinVUVpYC4k
QMMchQMc8j0aMA0GCSqGSIb3DQEBCwUAA4ICAQA0aAq/MSAHhNbpv43FpaztSOZ6
DIa/slREJkf6GBpo3jAdUCZTAnC7mptiIsK6TjzEfhCQf1grNjQuKxpsybWWU7Ol
zj+h5uqDPkDIuewzin277hgUvQ5sF7E2yvWr+XbDs8t3eBWzn2keZS6k3WFK8Cnr
imI1+bu8hybBnbwAI/F1ttTZlIBksyTGERUsc0eS+rqR0yFf0TPTzfv5ufxRmxdF
Fq8UToodPwOFdroiqI3PgUia58HfBewB76zYWAyOdfaFB1sSUDHjHLNkd/2HAGpu
EG9z8kogYNfGMuSqrZjqjzf/Bo+X11vhgOMCYcyyrK/gbtnmHlyafD6u01VTksJN
9obqtLR2N6DjOOokZMXmn95XPSMSkiVcfuEU7f9cfNzeWbwghMoSX6qnZnoiKMFo
ckP7lvnNhwPf7p6mI+dHPi6NeZfvd8WdB3/maJ+OhdCa7re/vz2Q4+hDd8P2+vbf
W8AgY2G1RQhd1CneTm5lqvbjvnea/xyojnq0zWTQk0+CU8RdUfGUBrPFzpB4lNox
quKCynFE1jlNia7m2OtJzNzo/W2kchvFzel6nwFQCjD2x9OawLBBpHCV+BT+9Df3
Hr7HCqT0SXpCWF1Tx0NZeenEhYvAJgr7zz+UnWGwM2HibZl71SBBWu4aR1zxgmF3
MibJvYfIK0LtY4j+fw==").run()
    

with Flow(name="job-flow-1") as flow:
    task = job1()

flow.storage = GitHub(
    repo="miguelferrao/test-flow",
    path="k8s_job.py",       
)

flow.run()
