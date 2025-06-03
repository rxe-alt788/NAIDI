from scraper.scrape import scrape_rss
from hasher.hash_article import hash_article
from blockchain_logger.log_to_chain import log_to_chain
import feedparser

def run_pipeline():
    rss_feeds = [
        "http://feeds.bbci.co.uk/news/rss.xml"
    ]

    for feed_url in rss_feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:  # Limit for test
            title = entry.title
            published = entry.published
            link = entry.link
            body = entry.get("summary", "")  # summary or content

            article_hash = hash_article(title, published, body)
            log_to_chain(article_hash, link)

if __name__ == "__main__":
    run_pipeline()

