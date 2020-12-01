#----------------------------------------------------------------------
# Functions for 2020 AGU Workshop tutorial notebooks
#
#----------------------------------------------------------------------

from netrc import netrc
from platform import system
from getpass import getpass
from urllib import request
from http.cookiejar import CookieJar
from os.path import join, expanduser
import requests
from pprint import pprint
import json
import os
import requests
from xml.etree import ElementTree as ET
import shutil
import time
import zipfile
import io


TOKEN_DATA = ("<token>"
              "<username>%s</username>"
              "<password>%s</password>"
              "<client_id>PODAAC CMR Client</client_id>"
              "<user_ip_address>%s</user_ip_address>"
              "</token>")


def setup_cmr_token_auth(endpoint: str='cmr.earthdata.nasa.gov'):
    ip = requests.get("https://ipinfo.io/ip").text.strip()
    return requests.post(
        url="https://%s/legacy-services/rest/tokens" % endpoint,
        data=TOKEN_DATA % (input("Username: "), getpass("Password: "), ip),
        headers={'Content-Type': 'application/xml', 'Accept': 'application/json'}
    ).json()['token']['id']


def setup_earthdata_login_auth(endpoint: str='urs.earthdata.nasa.gov'):
    netrc_name = "_netrc" if system()=="Windows" else ".netrc"
    try:
        username, _, password = netrc(file=join(expanduser('~'), netrc_name)).authenticators(endpoint)
    except (FileNotFoundError, TypeError):
        print('Please provide your Earthdata Login credentials for access.')
        print('Your info will only be passed to %s and will not be exposed in Jupyter.' % (endpoint))
        username = input('Username: ')
        password = getpass('Password: ')
    manager = request.HTTPPasswordMgrWithDefaultRealm()
    manager.add_password(None, endpoint, username, password)
    auth = request.HTTPBasicAuthHandler(manager)
    jar = CookieJar()
    processor = request.HTTPCookieProcessor(jar)
    opener = request.build_opener(auth, processor)
    request.install_opener(opener)
    
    
def get_harmony_results(harmony_url, token):
    """
    Performs a data customization and access request from Harmony.
    
    :harmony_url: Harmony asynchronous request URL. See https://harmony.earthdata.nasa.gov/docs/api/ for more information.
    :token: CMR token needed for restricted search
    
    """
    harmony_root = 'https://harmony.earthdata.nasa.gov'
    print('Request URL', harmony_url)
    with requests.Session() as session:
        r = session.get(harmony_url)
        harmony_response = r.content
        async_json = json.loads(harmony_response)
        #pprint(async_json)

        jobConfig = {
            'jobID': async_json['jobID']
        }

        job_url = harmony_root+'/jobs/{jobID}'.format(**jobConfig)
        print('Job URL', job_url)

        job_response = session.get(job_url)
        job_results = job_response.content
        job_json = json.loads(job_results)

        #Continue loop while request is still processing
        while job_json['status'] == 'running' and job_json['progress'] < 100: 
            print('Job status is running. Progress is ', job_json['progress'], '%. Trying again.')
            time.sleep(10)
            loop_response = session.get(job_url)
            loop_results = loop_response.content
            job_json = json.loads(loop_results)
            if job_json['status'] == 'running':
                continue

        if job_json['progress'] == 100:
            print('Job progress is 100%.')
            return job_json
        else: 
            return 