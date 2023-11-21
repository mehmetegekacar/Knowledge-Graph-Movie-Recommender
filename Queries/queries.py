# Define the SPARQL query to retrieve movies
sparql_query = """
    SELECT ?item ?name ?directorname ?genrename ?countryname 
    WHERE {
   ?item wdt:P31 wd:Q11424;
    wdt:P1476 ?name;
    wdt:P57 ?director;
    wdt:P136 ?genre;
    wdt:P495 ?country;
    wdt:P444 ?review.
  
    ?director rdfs:label ?directorname.
    ?genre rdfs:label ?genrename.
    ?country rdfs:label ?countryname.
  
  FILTER(LANG(?directorname) = "en")
  FILTER(LANG(?name)="en")
  FILTER(LANG(?genrename)="en")
  FILTER(LANG(?countryname)="en")
  
}
LIMIT 10
    """

query_wikidata_director = """
SELECT ?item ?name
WHERE {
  ?item wdt:P31 wd:Q11424;
      wdt:P57 ?x.
  ?x rdfs:label "Christopher Nolan"@en.
  ?item rdfs:label ?name.
  filter(lang(?name)="en")
}
LIMIT 100 
"""

def query_genre(x: str, number: int = 10):
    query = """
    SELECT ?item ?name ?directorname ?genrename ?countryname ?year
    WHERE {{
        ?item wdt:P31 wd:Q11424;
            wdt:P136 ?genre;
            wdt:P1476 ?name;
            wdt:P57 ?director;
            wdt:P136 ?genre;
            wdt:P495 ?country;
            wdt:P577 ?year.
        
        ?director rdfs:label ?directorname.
        ?genre rdfs:label ?genrename.
        ?country rdfs:label ?countryname.

            ?genre rdfs:label "{}"@en.
            ?item rdfs:label ?name.

            FILTER(LANG(?name)="en")
            FILTER(LANG(?directorname) = "en")
            FILTER(LANG(?genrename)="en")
            FILTER(LANG(?countryname)="en")
    }}
    LIMIT {}
    """.format(x, number)
    return query

def query_country(x: str, number: int = 10):
    query = """
    SELECT ?item ?name ?directorname ?genrename ?countryname ?year
    WHERE {{
        ?item wdt:P31 wd:Q11424;
          wdt:P495 ?country;
          wdt:P136 ?genre;
          wdt:P1476 ?name;
          wdt:P57 ?director;
          wdt:P577 ?year.  

        ?director rdfs:label ?directorname.
        ?genre rdfs:label ?genrename.
        ?country rdfs:label ?countryname.

        ?country rdfs:label "{}"@en.
        ?item rdfs:label ?name.

        FILTER(LANG(?name)="en")
            FILTER(LANG(?directorname) = "en")
            FILTER(LANG(?genrename)="en")
            FILTER(LANG(?countryname)="en")
    }}
    LIMIT {}
    """.format(x, number)
    return query

def query_director(x: str, number: int = 10):
    query = """
    SELECT ?item ?name ?directorname ?genrename ?countryname ?year
    WHERE {{
        ?item wdt:P31 wd:Q11424;
              wdt:P495 ?country;
          wdt:P136 ?genre;
          wdt:P1476 ?name;
            wdt:P57 ?director;
            wdt:P577 ?year. 


        ?director rdfs:label ?directorname.
        ?genre rdfs:label ?genrename.
        ?country rdfs:label ?countryname.

        ?director rdfs:label "{}"@en.
        ?item rdfs:label ?name.
        FILTER(LANG(?name)="en")
            FILTER(LANG(?directorname) = "en")
            FILTER(LANG(?genrename)="en")
            FILTER(LANG(?countryname)="en")
    }}
    LIMIT {}
    """.format(x, number)
    return query

def query_actor(x:str, number: int=10):
    query = """
    SELECT ?item ?name ?directorname ?genrename ?countryname ?year
    WHERE {{
        ?item wdt:P31 wd:Q11424;
              wdt:P495 ?country;
          wdt:P136 ?genre;
          wdt:P1476 ?name;
            wdt:P57 ?director;
            wdt:P577 ?year. 


        ?director rdfs:label ?directorname.
        ?genre rdfs:label ?genrename.
        ?country rdfs:label ?countryname.

        ?actor rdfs:label "{}"@en.
        ?item rdfs:label ?name.
        FILTER(LANG(?name)="en")
            FILTER(LANG(?directorname) = "en")
            FILTER(LANG(?genrename)="en")
            FILTER(LANG(?countryname)="en")
    }}
    LIMIT {}
    """.format(x, number)
    return query

def query_year(x:str, number:int=10):
    query = """
    SELECT ?item ?name ?directorname ?genrename ?countryname ?year
    WHERE {{
        ?item wdt:P31 wd:Q11424;
        wdt:P495 ?country;
        wdt:P136 ?genre;
        wdt:P1476 ?name;
        wdt:P57 ?director;
        wdt:P577 ?year. 


        ?director rdfs:label ?directorname.
        ?genre rdfs:label ?genrename.
        ?country rdfs:label ?countryname.

        ?item rdfs:label ?name.
        FILTER(LANG(?name)="en")
            FILTER(LANG(?directorname) = "en")
            FILTER(LANG(?genrename)="en")
            FILTER(LANG(?countryname)="en")
        FILTER(YEAR(?date) = {})
    }}
    LIMIT {}
    """.format(x, number)
    return query


def one_to_one_match_query(director, genre, country, year, number: int=10):
    query = """
SELECT ?item ?name ?directorname ?genrename ?countryname ?year
WHERE {{
   ?item wdt:P31 wd:Q11424;
    wdt:P1476 ?name;
    wdt:P57 ?director;
    wdt:P136 ?genre;
    wdt:P495 ?country;
    wdt:P577 ?year.
  
  ?director rdfs:label {}.
  ?genre rdfs:label {}.
  ?country rdfs:label {}.
  
  FILTER(LANG(?year)="en")
  FILTER(LANG(?directorname) = "en")
  FILTER(LANG(?name)="en")
  FILTER(LANG(?genrename)="en")
  FILTER(LANG(?countryname)="en")
  FILTER(year(?year) = {})
}}
LIMIT {}
""".format(director, genre, country, year, number)
    return query

def optional_match_query(director, genre, country, year, number: int=10):
    query = """
 SELECT ?item ?name ?directorname ?genrename ?countryname ?year ?yearLiteral
WHERE {{
  ?item wdt:P31 wd:Q11424;
    wdt:P1476 ?name;
    wdt:P57 ?director;
    wdt:P136 ?genre;
    wdt:P495 ?country;
    wdt:P577 ?year.
  
  OPTIONAL {{
    ?item wdt:P577 ?yearLiteral.
    FILTER(year(?yearLiteral) = {})
  }}

  OPTIONAL {{ ?director rdfs:label "{}"@en. }}
  OPTIONAL {{ ?genre rdfs:label "{}"@en. }}
  OPTIONAL {{ ?country rdfs:label "{}"@en. }}
  
  FILTER(LANG(?directorname) = "en")
  FILTER(LANG(?name) = "en")
  FILTER(LANG(?genrename) = "en")
  FILTER(LANG(?countryname) = "en")
}}
LIMIT {}
""".format(year, director, genre, country, number)
    return query