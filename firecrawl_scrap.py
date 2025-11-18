from firecrawl import Firecrawl

firecrawl = Firecrawl(
    api_key="fc-",
)

# Scrape a website:
docs = firecrawl.crawl(url="https://www.doordash.com/?srsltid=AfmBOoqK6xPTKysYtmIo4wanVUZu3egYkguTUb7qPx8WSQmBUSeIAoA2", limit=10)
print(docs)


