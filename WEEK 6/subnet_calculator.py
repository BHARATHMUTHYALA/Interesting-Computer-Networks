import ipaddress
def subnet_calculator(cidr_input):
    try:
        network = ipaddress.ip_network(cidr_input, strict = False)
        print(f"\n Subnet calculation for {cidr_input}")
        print(f"Network address: {network.network_address}")
        print(f"Broadcast_Address : {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Wildcard  Mask: {network.hostmask}")
        print(f"Number of hosts: {network.num_addresses - 2}")
        print("Usable Host IPs :")
        
        for ip in network.hosts():
            print(ip)
            
    except ValueError as e:
        print(f"Invalid input : {e}")
        
cidr = input("Enter IP Address in CIDR notation ")
subnet_calculator(cidr)
