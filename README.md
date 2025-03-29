# domain_availibily_aws
Search available domains names from the list input from text file 
I am using WSL Ubuntu.

You can use Ubuntu OS in VM or EC2:

Dependency Installation :
 
sudo apt install python3
sudo apt install python3-venv -y

Create Python Virtual env for running scripts:

python3 -m venv ~/domain_checker_venv

source ~/domain_checker_venv/bin/activate  # Activate the venv

Install the required Binaries:
pip install boto3 pandas tqdm python-whois

Configure AWS credentials :

command : aws configure

Install awscli if its missing.

Kindly check various ways to do it.

Now I using basic aws config and credentials in below :

PWD : .aws 

drwxr-xr-x  2 ffasf ffasf 4096 Mar 10 02:16 ./
drwxr-x--- 17 ffasf ffasf 4096 Mar 29 05:12 ../
-rw-------  1 ffasf ffasf   29 Mar 29 02:44 config
-rw-------  1 ffasf ffasf  116 Mar 21 06:42 credentials

To search a domain for its availability 

You can pass input file as below with searchable domain names :

python3 domain_checker.py --input health_domains.txt --output available_health_domains.csv

Sample of the texfile something like below : 
mydomain.com
xydomdain.com
mynexusrepo.com


Error Handling:

Silently skips domains that cause errors
Tracks and reports number of errors at the end

Clean Output:
Only writes successfully checked available domains
Provides clear summary of results

Efficiency:
Still uses progress bar (tqdm)
Minimal memory usage

Formatting:
Proper CSV formatting with header row
Clean console output

Script to check the price of availability domains

Next steps is you can write python to register these domains after finding if they are available.

The whole story is to register domains which might be in demand for future .

EX : below domains are pricy 

💰 Recently Sold High-Priced Health Domains
Domain	Reported Sale Price	Buyer/Use Case
Cannabis.com	$9M (2019)	Marijuana industry
Insure.com	$16M (2009)	Insurance sector
Voice.com	$30M (2019)	Blockchain/Voice tech
Med.com	$4M+ (Est.)	Healthcare giant
AI.org	$5M+ (Est.)	AI industry


