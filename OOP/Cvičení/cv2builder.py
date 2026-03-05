class ServerConfiguration:
    def __init__(self):
        self.host = None
        self.port = None
        self.ssl = None
        self.timeout = None
        self.max_connections = None
        self.logging = None

    def set_host(self, host: str):
        self.host = host
        return self 
    
    def set_port(self, port: str):
        self.port = port
        return self
    
    def set_ssl(self, ssl: str):
        self.ssl = ssl
        return self
    
    def set_timeout(self, timeout:str):
        self.timeout = timeout
        return self
    
    def set_max_connections(self, max_connections: str):
        self.max_connections = max_connections
        return self
    
    def set_logging(self, logging: str):
        self.logging = logging
        return self

    def __str__(self) -> str:
        return (
            f"ServerConfiguration(host='{self.host}', port={self.port}, ssl={self.ssl}, "
            f"timeout={self.timeout}, max_connections={self.max_connections}, logging={self.logging})"
        )


if __name__ == "__main__":
    config = ServerConfiguration().set_host("0.0.0.0").set_port(443).set_ssl(True).set_timeout(10).set_max_connections(100).set_logging(True)
    print(config)
    

    