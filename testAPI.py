import json

import pytest

import requests

def test_getStem_chkforwords():
    movies = "stem"

    url = "http://www.omdbapi.com/?i=&apikey=1d094a12&s=" + movies + "*&page=2&type=movie"
    print(url)
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload).text
    payload={}
    headers = {}
    assert 'stem' in str(response)

def test_getSTEMchkhowlong():
    movies = "stem"

    url = "http://www.omdbapi.com/?i=&apikey=1d094a12&s=" + movies + "*&page=2&type=movie"
    print(url)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).text
    response_dict = json.loads(response)
    print("---------",response_dict)

    for k in response_dict:

        print("---K----",k,  response_dict[k])

        if "stemA" in  response_dict[k]:
            assert "Pass"
            print("pass")
        if k == "totalResults":
            total = int(response_dict[k].split("_")[0])
            assert total >=31

            if total >= 0:

                print("Wowow")





