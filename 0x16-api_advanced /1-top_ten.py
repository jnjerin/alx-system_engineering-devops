#!/usr/bin/python3
'''
 Prints the titles of the first 10 hot
 posts listed for a given subreddit.
'''
import requests
import json
import sys
def top_ten(subreddit):
    """
    Retrieves the titles of the top 10 hot posts in a subreddit.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        None if an error occurs, otherwise prints titles of the top 10 posts.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = "reddit_user"

    headers = {"User-Agent": user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json()
        children = data.get("data", {}).get("children", [])  # Handle potential missing keys

        for post in children[:10]:
            print(post["data"]["title"])

    except json.JSONDecodeError:
        print("Error: Invalid JSON response")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a subreddit name as an argument.")
    else:
        top_ten(sys.argv[1])