import time
import json
import os

REGISTRY_PATH = os.path.join(os.path.dirname(__file__), '../registry/registry.json')

def log_to_chain(article_hash, source_url):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    record = {
        "hash": article_hash,
        "source": source_url,
        "timestamp": timestamp
    }

    # Load existing records
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Avoid duplicates
    if not any(r["hash"] == article_hash for r in data):
        data.append(record)
        with open(REGISTRY_PATH, "w") as f:
            json.dump(data, f, indent=2)
        print("✅ Logged to chain (mock):", record)
    else:
        print("ℹ️ Hash already logged.")

    return record

# Example
if __name__ == "__main__":
    fake_hash = "abc123deadbeef456789"
    source_url = "https://example.com/article"
    log_to_chain(fake_hash, source_url)
