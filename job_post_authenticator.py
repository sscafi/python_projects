import requests
from bs4 import BeautifulSoup

def validate_job_posting(job_title, company_name, job_board_url):
    try:
        # Step 1: Fetch the job board page HTML
        response = requests.get(job_board_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        # Step 2: Parse HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Step 3: Find job postings and verify details
        job_postings = soup.find_all(class_='job-posting')  # Adjust class or tag based on the job board HTML structure

        found_matching_posting = False
        for posting in job_postings:
            title = posting.find(class_='job-title').text.strip()
            company = posting.find(class_='company-name').text.strip()

            if job_title.lower() in title.lower() and company_name.lower() in company.lower():
                found_matching_posting = True
                break

        if found_matching_posting:
            print(f"The job posting for '{job_title}' at '{company_name}' on {job_board_url} is authentic.")
            return True
        else:
            print(f"No authentic job posting found for '{job_title}' at '{company_name}' on {job_board_url}.")
            return False
    
    except requests.RequestException as e:
        print(f"Error fetching job board page: {e}")
        return False
    
    except (AttributeError, KeyError) as e:
        print(f"Error parsing job board page: {e}")
        return False

# Example usage:
job_title = "Software Engineer"
company_name = "Example Company"
job_board_url = "https://examplejobboard.com"

validate_job_posting(job_title, company_name, job_board_url)
