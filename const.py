TOP_HEADLINES_URL = "https://newsapi.org/v2/top-headlines"
EVERYTHING_URL = "https://newsapi.org/v2/everything"
SOURCES_URL = "https://newsapi.org/v2/sources"

#: The 2-letter ISO 3166-1 code of the country you want to get headlines for.  If not specified,
#: the results span all countries.
countries = {
    "United States ": "us",
    "USA ": "us",
    "US": "us",
    "us": "us",
    "GBR": "gb",
    "UK" : "gb",
    "uk" : "gb"
}

languages = {"ar", "en", "cn", "de", "es", "fr", "he", "it", "nl", "no", "pt", "ru", "sv", "se", "ud", "zh"}


categories = {"business", "entertainment", "general", "health", "science", "sports", "technology"}

#: The order to sort article results in.  If not specified, the default is ``"publishedAt"``.
sort_method = {"relevancy", "popularity", "publishedAt"}

def lookup_table(input_country):
    return countries[input_country]
