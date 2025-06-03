import feedparser

# List of RSS feeds from news sources
rss_feeds = [
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
]

def scrape_rss():
    for feed_url in rss_feeds:
        feed = feedparser.parse(feed_url)
        print(f"\n--- Articles from {feed_url} ---\n")
        for entry in feed.entries[:5]:  # Just show first 5 articles
            print("Title:", entry.title)
            print("Link:", entry.link)
            print("Published:", entry.published)
            print("-" * 40)

if __name__ == "__main__":
    scrape_rss()

