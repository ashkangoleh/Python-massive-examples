"""
need to install first "sudo apt-get install graphviz"
"""


from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import PostgreSQL
from diagrams.aws.network import ELB
from diagrams.aws.compute import EC2, ECS
from diagrams.onprem.workflow import Airflow
from diagrams.azure.storage import TableStorage
from diagrams.k8s.controlplane import Sched
from diagrams.oci.monitoring import Queue
from diagrams.onprem.queue import Celery
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import Python
from diagrams.onprem.monitoring import Prometheus,Grafana
from diagrams.onprem.network import Traefik
from diagrams.onprem.container import Docker
with Diagram("Blockchair Data source", show=False, filename="blockchair_source_pipeline", direction="LR"):
    metrics = Prometheus("metric")
    metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")
    python = Python("Dag Directory")
    with Cluster("Extract"):
        extract = ELB("Blockchair dumps")

    with Cluster("Load"):
        psql = PostgreSQL("Source DB")

        with Cluster("Tables"):
            outputs = TableStorage("Outputs")
            inputs = TableStorage("Inputs")
            transactions = TableStorage("Transactions")
            blocks = TableStorage("Blocks")

    with Cluster("Transform"):
        airflow = Airflow("Orchestrator Engine")

    with Cluster("Airflow"):
        with Cluster("DB"):
            psql_metadata_db = PostgreSQL("Metadata DB")
        with Cluster("Background tasks"):
            scheduler = Sched("Scheduler")
            executor = EC2("Executor")
        with Cluster("Master Node"):
            webserver = ECS("Web server")

    queue = Queue()
    with Cluster("Worker node 1"):
        worker_1 = EC2()

    with Cluster("Worker node 2"):
        worker_2 = EC2()

    with Cluster("Worker node 3"):
        worker_3 = EC2()

    webserver >> Edge(color="darkgray") << psql_metadata_db
    scheduler >> Edge(color="darkgray") << psql_metadata_db
    scheduler >> executor
    executor >> Redis() >> Celery() >> queue
    queue >> [worker_1, worker_2, worker_3]
    python >> webserver

    extract >> airflow >> psql >> [
        outputs, inputs, transactions, blocks]<< metrics 
