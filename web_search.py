## Use DuckDuckGo
## Get List of DATA

from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults(output_format="list")

# use `.run()` (common method) and capture/print the result
result = search.run("Mobile Apps Food Delivery")
print(result)