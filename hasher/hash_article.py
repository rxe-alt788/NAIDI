import hashlib

def hash_article(title, published, body):
    content = f"{title}|{published}|{body}"
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

# Example usage
if __name__ == "__main__":
    title = "Example Headline"
    published = "2025-06-03T12:00:00Z"
    body = "This is a test article body for NAID prototype."

    article_hash = hash_article(title, published, body)
    print("SHA-256 Hash:", article_hash)

