"""
need to install first "sudo apt-get install graphviz"
"""


from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import PostgreSQL
from diagrams.custom import Custom
from diagrams.aws.compute import EC2
from diagrams.programming.language import Python
from diagrams.onprem.client import Users
from diagrams.onprem.network import Traefik
from diagrams.onprem.container import Docker
from diagrams.programming.framework import Fastapi

with Diagram("Blockchair Data Services", show=False, filename="services", direction="LR"):
    
    # python = Python("")
    with Cluster("DB Containers"):
        db_docker = Docker()
        with Cluster("DB Sources"):
            raw_database = PostgreSQL("Raw")
            history_database = PostgreSQL("History")
    with Cluster("Service Container"):
        service_docker = Docker()
        with Cluster("Service"):
            fastapi = Fastapi("FastAPI")
            uvicorn = Custom("Webserver",'./uvicorn.png')
    with Cluster("Client Side"):
         swagger = Custom("Swagger",'./swagger.png')
         redoc = Custom("Redoc",'./redoc.png')
    with Cluster("Proxy Container"):
        Proxy_docker = Docker()
        with Cluster('CNAP(cloud-native application networking)'):
            traefik = Custom("Traefik",'./traefik.png')
        
    [raw_database,history_database] >> Edge(color="red") << fastapi >> uvicorn >> traefik >> [swagger,redoc] >> Users("Clients")
        
    