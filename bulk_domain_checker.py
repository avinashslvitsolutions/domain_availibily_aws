import boto3
import csv
from tqdm import tqdm

# Initialize AWS Client
client = boto3.client('route53domains', region_name='us-east-1')

def check_availability(domain):
    try:
        response = client.check_domain_availability(DomainName=domain)
        return response['Availability']
    except Exception:
        return "ERROR"

# Read domains from input file
with open("domains.txt") as f:
    domains = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Check domains
available_domains = []
error_count = 0

for domain in tqdm(domains, desc="Checking domains"):
    status = check_availability(domain)
    if status == "AVAILABLE":
        available_domains.append(domain)
    elif status == "ERROR":
        error_count += 1
        continue  # Skip error domains

# Save results
if available_domains:
    with open("available_domains.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Domain"])  # Header
        writer.writerows([[domain] for domain in available_domains])
    
    print(f"\n✅ Results:")
    print(f"- Available: {len(available_domains)} (saved to 'available_domains.csv')")
    print(f"- Errors: {error_count} domains skipped")
else:
    print("\n❌ No available domains found.")
    if error_count > 0:
        print(f"- Encountered errors with {error_count} domains")
