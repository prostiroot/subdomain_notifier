# subdomain_notifier
send an email when new subdomain is registered for a domain in list_of_domains.txt file.

it will:
1) look into list_of_domains.txt file
2) run subdomain enumeration tools against a domain in list_of_domains.txt file
3) merge results to one result file
4) compare result file to known subdomains list for that domain
5) send an email if there are new subdomains

# how to set it up
1) Clone repo
2) Create a gmail account for sending out emails
  - adjust your gmail account’s security settings to allow access: turn "Allow less secure apps" to ON
3) add your email data to email_config.json.example and rename it to email_config.json
4) add your domains to list_of_domains.txt.example and rename it to list_of_domains.txt
  - do not add protocol or "www", just domain.com is fine
5) Download tools (tools/ folder):
  - script "run_subdomain_search.sh" is currently using 3: amass, sublist3r and findomain
6) modify "run_subdomain_search.sh" according to your tools if necessary
7) set up cron job (crontab -e):
 - example to run job every 3 hours:
 
30 */3 * * * cd /path/to/subdomain_notifier && ./run_subdomain_search.sh && python3 notifier.py
