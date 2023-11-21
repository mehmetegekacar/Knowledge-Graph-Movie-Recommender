import requests
from rdflib import Graph, Namespace, Literal, URIRef
import pandas as pd

def query_wikidata_sparql(sparql_query):
    # Wikidata SPARQL endpoint
    endpoint_url = "https://query.wikidata.org/sparql"

    # Headers with user agent information (Wikimedia recommends providing a User-Agent header)
    headers = {
        'User-Agent': 'YourBot/1.0 (your@email.com)',
        'Accept': 'application/json'
    }

    # Query parameters
    params = {
        'query': sparql_query,
        'format': 'json'
    }

    # Make the request to Wikidata SPARQL endpoint
    response = requests.get(endpoint_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and return the JSON response
        return response.json()
    else:
        # If the request was not successful, print the error code
        print(f"Error: {response.status_code}")
        return None

def save_output_results(results):
    empty = {"name": [], "directorname": [], "genrename": [], "countryname": [], "year": []}
    for i in results["results"]["bindings"]:
        empty["name"].append(i["name"]["value"])
        empty["directorname"].append(i["directorname"]["value"])
        empty["genrename"].append(i["genrename"]["value"])
        empty["countryname"].append(i["countryname"]["value"])
        empty["year"].append(i["year"]["value"])
    return pd.DataFrame(empty, columns=["name", "directorname", "genrename", "countryname", "year"])

def output_query(sparql_query):
    result = query_wikidata_sparql(sparql_query)
    df = save_output_results(result)
    return df
