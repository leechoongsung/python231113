import requests
from bs4 import BeautifulSoup

def naver_blog_crawler(search_keyword):
    base_url = "https://search.naver.com/search.naver"
    params = {
        "where": "view",
        "sm": "tab_jum",
        "query": search_keyword
    }

    # Send a GET request to the Naver search URL
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information from the search results
        blog_results = soup.find_all('li', class_='sh_blog_top')

        for result in blog_results:
            # Extract information from each blog result
            blog_address = result.find('a', class_='sh_blog_title').get('href')
            blog_name = result.find('a', class_='txt84').text
            post_title = result.find('a', class_='sh_blog_title').text
            post_date = result.find('span', class_='txt84').text

            # Print the extracted information
            print(f"Blog Address: {blog_address}")
            print(f"Blog Name: {blog_name}")
            print(f"Post Title: {post_title}")
            print(f"Posting Date: {post_date}")
            print("="*50)

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Example usage
search_keyword = "iPhone 15"
naver_blog_crawler(search_keyword)



