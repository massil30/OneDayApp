## Use DuckDuckGo
## Get List of DATA

from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults(output_format="list")

search.invoke("Mobile Apps Food Delivery")