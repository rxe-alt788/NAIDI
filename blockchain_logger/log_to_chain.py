import time

# This is a MOCK version – no blockchain yet, just simulates a log
def log_to_chain(article_hash, source_url):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    record = {
        "hash": article_hash,
        "source": source_url,
        "timestamp": timestamp
    }
    print("✅ Logged to chain (mock):", record)
    return record

# Example usage
if __name__ == "__main__":
    fake_hash = "abc123deadbeef456789"
    source_url = "https://example.com/article"
    log_to_chain(fake_hash, source_url)

