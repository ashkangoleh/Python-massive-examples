import os


class ApiClient:

    def __init__(self, api_key: str, timeout: int) -> None:
        self.api_key = api_key  # <-- dependency is injected
        self.timeout = timeout  # <-- dependency is injected

    def __repr__(self) -> str:
        return f"{self.api_key},{self.timeout}"


class Service:

    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client  # <-- dependency is injected
    def __repr__(self) -> str:
        return repr(self.api_client)

def main(service: Service) -> None:  # <-- dependency is injected
    return service


if __name__ == "__main__":
    print(main(
        service=Service(
            api_client=ApiClient(
                api_key="API_KEY",
                # api_key=os.getenv("API_KEY"),
                timeout=12,
                # timeout=int(os.getenv("TIMEOUT")),
            ),
        ),
    )
    )
