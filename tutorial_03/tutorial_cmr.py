# This cell to be moved to module
import requests

def search_granules(search_parameters, geojson=None, output_format="json"):
    """
    Performs a granule search
    
    :search_parameters: dictionary of CMR search parameters
    :geojson: filepath to GeoJSON file for spatial search
    :output_format: select format for results https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html#supported-result-formats
    
    :returns: if hits is greater than 0, search results are returned in chosen output_format, otherwise returns None.
    """
    search_url = "https://cmr.earthdata.nasa.gov/search/granules"
    
    if geojson:
        files = {"shapefile": (geojson, open(geojson, "r"), "application/geo+json")}
    else:
        files = None
        
    parameters = {
        "scroll": "true",
        "page_size": 100,
    }
    
    try:
        response = requests.post(f"{search_url}.{output_format}", params=parameters, data=search_parameters, files=files)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP Error: {http_error}")
    except Exception as err:
        print(f"Error: {err}")
    
    hits = int(response.headers['CMR-Hits'])
    if hits > 0:
        print(f"Found {hits} granules")
        return response
    else:
        print("Found no hits")
        return


def filter_urls(response):
    """
    Extracts urls for each granule
    
    :response: json structure returned by search_granules
    
    :returns: list of urls or empty list if no entries
    """
    if 'feed' not in search_results or 'entry' not in search_results['feed']:
        return []

    entries = [e['links']
               for e in search_results['feed']['entry']
               if 'links' in e]
    # Flatten "entries" to a simple list of links
    links = list(itertools.chain(*entries))

    urls = []
    unique_filenames = set()
    for link in links:
        if 'href' not in link:
            # Exclude links with nothing to download
            continue
        if 'inherited' in link and link['inherited'] is True:
            # Why are we excluding these links?
            continue
        if 'rel' in link and 'data#' not in link['rel']:
            # Exclude links which are not classified by CMR as "data" or "metadata"
            continue

        if 'title' in link and 'opendap' in link['title'].lower():
            # Exclude OPeNDAP links--they are responsible for many duplicates
            # This is a hack; when the metadata is updated to properly identify
            # non-datapool links, we should be able to do this in a non-hack way
            continue

        filename = link['href'].split('/')[-1]
        if filename in unique_filenames:
            # Exclude links with duplicate filenames (they would overwrite)
            continue
        unique_filenames.add(filename)

        urls.append(link['href'])

    return urls


