
from googlesearch import search

def search_func(query,  advanced=True):
    search_result_return = []
    search_results = search(query, num_results=3, advanced=True)
    for result in search_results:
        search_result_return.append(result)
    return search_result_return
