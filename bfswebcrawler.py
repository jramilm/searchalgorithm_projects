import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin

def get_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # extract all 'a' tags and get href attribute
        links = set()

        for a_tag in soup.find_all("a", href=True):
            link = a_tag["href"]
            full_link = urljoin(url, link)

            if full_link.startswith("http"):
                links.add(full_link)

        return links
    
    except requests.RequestException as e:
        print(f"Failed to access {url}: {e}")
        return set()

def search_keyword(url, keyword):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        # try to get all text content from the page
        page_text = soup.get_text().lower()

        if keyword.lower() in page_text:
            return True
        return False
    
    except requests.Timeout:
        print(f"Request to {url} timed out. Skipping...")
    
    except requests.RequestException as e:
        print(f"Failed to access {url}: {e}")
        return False

def bfs_crawler(start_url, keyword, max_depth=3, max_pages=100):
    visited = set()  
    queue = deque([(start_url, 0)])  
    page_count = 0
    
    while queue and page_count < max_pages:
        url, depth = queue.popleft()  
        if depth > max_depth:  
            break
        
        if url in visited:
            continue
        
        print(f"Visiting: {url} (depth: {depth})")

        visited.add(url)
        page_count+=1
        
        if search_keyword(url, keyword):
            print(f"Keyword '{keyword}' found on page: {url}")
            return url
        
        links = get_links(url)

        for link in links:
            if link not in visited:
                queue.append((link, depth + 1))
    
    print(f"Keyword '{keyword}' not found within depth limit.")
    return None

start_url = input("Enter the start URL: ") # always include "https://" here
keyword = input("Enter the keyword to search: ")

result_url = bfs_crawler(start_url, keyword)

if result_url:
    print(f"The keyword was found at: {result_url}")
else:
    print("No result found within the search depth.")
