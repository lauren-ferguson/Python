# MULTITHREAD PORT SCANNER
# Returns True if a connection can be made, False otherwise
def test_port_number(host, port):
    with socket(AF_INET, SOCK_STREAM) as sock:  # Create socket
        sock.settimeout(3)  # Timeout
        try:
            sock.connect((host, port))
            return True # Successful connection
        except:
            return False  # Ignore failure


# Scan ports on host
def port_scan(host, ports):
    print(f'Scanning {host}...')
    with ThreadPoolExecutor(len(ports)) as executor:  # Create threadpool
        results = executor.map(test_port_number, [host] * len(ports), ports)  # Dispatch tasks
        for port, is_open in zip(ports, results):  # Report results
            if is_open:
                print(f'{port} open')


# Input host and define ports
HOST = input("Please input website URL ")  # Input host
PORTS = range(65535)
port_scan(HOST, PORTS)  # Test ports
