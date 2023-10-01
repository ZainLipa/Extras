# Program of the Day: URL Shortener

import hashlib

def shorten_url(url):
    # Hash the URL using MD5
    hashed = hashlib.md5(url.encode()).hexdigest()

    # Take the first 8 characters of the hash as the short URL
    short_url = hashed[:8]

    return short_url

# Example usage
long_url = "https://www.example.com/a/very/long/url"
short_url = shorten_url(long_url)

print(f"Long URL: {long_url}")
print(f"Short URL: https://short.url/{short_url}")
