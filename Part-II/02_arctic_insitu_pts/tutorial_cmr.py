# This cell to be moved to module
import os
import requests
import itertools
import netrc
import getpass
from urllib.parse import urlparse

from shapely.geometry import Polygon
import pandas as pd
import geopandas

URS_URL = 'https://urs.earthdata.nasa.gov'


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
        return response.json()
    else:
        print("Found no hits")
        return


def filter_urls(search_results):
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


def print_urls(response):
    """
    Print list of href urls for granules from response
    
    :response: JSON structure from search_granules
    """
    for url in filter_urls(response):
        print(url)
    return


def filter_spatiotemporal(search_results):
    """
    Returns a list of dictionaries containing time_start, time_end and extent polygons for granules

    :search_results: dictionary object returned by search_granules
    
    :returns: list of dictionaries or empty list of no entries or keys do not exist
    """
    if 'feed' not in search_results or 'entry' not in search_results['feed']:
        return []
    
    def _extractor(mydict, key_list=["producer_granule_id", "time_start", "time_end", "polygons"]):
        """Extract spatio-temporal metadata from search results entry"""
        return {k: mydict.get(k, None) for k in key_list}

    subset = []
    for entry in search_results["feed"]["entry"]:
        subset.append(_extractor(entry))
    
    return subset


def polygon_to_geometry(polygon_entry):
    L = [float(s) for s in list(itertools.chain.from_iterable(polygon_entry))[0].split()]
    return Polygon( list(zip(L[1::2], L[::2])) )  # CMR returns JSON with latitude first  


def results_to_geodataframe(search_results, crs="EPSG:4326"):
    """
    Converts spatiotemporal fields from results to geopandas DataFrame
    
    :search_results: returned by search_granules
    :crs: coordinate reference system: default is WGS84 (EPSG:4326)
    
    :returns: geopandas dataframe with polygons field as geometry
    """
    
    results_dict = filter_spatiotemporal(search_results)
    if not results_dict:
        return
    
    df = pd.results_df = pd.DataFrame(results_dict)
    df["geometry"] = [polygon_to_geometry(entry["polygons"]) for entry in results_dict]
    return geopandas.GeoDataFrame(df, crs=crs)
    

def get_username():
    username = ''

    # For Python 2/3 compatibility:
    try:
        do_input = raw_input  # noqa
    except NameError:
        do_input = input

    while not username:
        try:
            username = do_input('Earthdata username: ')
        except KeyboardInterrupt:
            quit()
    return username


def get_password():
    password = ''
    while not password:
        try:
            password = getpass.getpass('password: ')
        except KeyboardInterrupt:
            quit()
    return password


def get_credentials():
    """Get user credentials from .netrc or prompt for input."""
    credentials = None
    errprefix = ''
    try:
        info = netrc.netrc()
        username, account, password = info.authenticators(urlparse(URS_URL).hostname)
        errprefix = 'netrc error: '
    except Exception as e:
        if (not ('No such file' in str(e))):
            print('netrc error: {0}'.format(str(e)))
        username = None
        password = None
        
    if not username:
        username = get_username()
        password = get_password()

    return (username, password)


def download(urls, outpath=''):
    """Download files from list of urls."""
    if not urls:
        return

    url_count = len(urls)
    print('Downloading {0} files to {1}...'.format(url_count, outpath))
    username = None

    for index, url in enumerate(urls, start=1):
        if not username and urlparse(url).scheme == 'https':
            username, password = get_credentials()

        filename = os.path.join(outpath, url.split('/')[-1])
        print('{0}/{1}: {2}'.format(str(index).zfill(len(str(url_count))),
                                    url_count,
                                    filename))

        try:
            response = requests.get(url, auth=(username, password))
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP Error: {http_error}")
        except Exception as err:
            print(f"Error: {err}")
        except KeyboardInterrupt:
            quit()
        else:
            open(filename, 'wb').write(response.content)

            
