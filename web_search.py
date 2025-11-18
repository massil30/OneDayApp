## Use DuckDuckGo
## Get List of DATA

from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults(output_format="list", timeout=20)  # 20 seconds
result = search.run("Mobile Apps Food Delivery")
print(result)
