#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers for a subreddit.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        The number of subscribers (integer) or 0 if an error occurs or the 
        subreddit is invalid.
    """

    url = f"https://reddit.com/r/{subreddit}/about.json"
    user_agent = "reddit_user"  # Custom User-Agent

    headers = {"User-Agent": user_agent}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)  # Handle potential missing keys

    except requests.exceptions.RequestException as e:
        print(f"Error getting subscriber count: {e}")
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(sys.argv[1])
        print(subscribers)
