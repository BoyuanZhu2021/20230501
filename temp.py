import socket
import dns.resolver

# Function to query DNS records for a given domain
def query_dns_records(domain):
    try:
        # Use dnspython's resolver to get 'A' records for the domain
        dns_records = dns.resolver.resolve(domain, 'A')
        print(f"DNS records for {domain}:")

        # Loop through the returned records and print the IP addresses
        for record in dns_records:
            print(record.address)
    except Exception as e:
        print(f"Error querying DNS records for {domain}: {e}")

# Function to perform a reverse DNS lookup for a given IP address
def reverse_dns_lookup(ip_address):
    try:
        # Use the socket library to get the host name from the IP address
        reversed_dns = socket.gethostbyaddr(ip_address)
        print(f"Reverse DNS lookup for {ip_address}: {reversed_dns[0]}")
    except Exception as e:
        print(f"Error performing reverse DNS lookup for {ip_address}: {e}")

# Main function that drives the script
def main():
    # Set the domain to query
    domain = "amazon.com"

    # Query DNS records for the specified domain
    query_dns_records(domain)

    # Ask the user to input an IP address for reverse DNS lookup
    ip_address = input("Enter an IP address for reverse DNS lookup: ")

    # Perform reverse DNS lookup for the specified IP address
    reverse_dns_lookup(ip_address)

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
