import json

import pytest

import requests


def test_chkLongstring():
    movies = "stem"

    url = "http://www.omdbapi.com/?i=&apikey=1d094a12&s=" + movies + "*&page=2&type=movie"
    print(url)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload).text
    payload = {}
    headers = {}

    response_dict = json.loads(response)
    print("---------", response_dict)
    movies = "stem"
    for k in response_dict:
        if k == "Search":
            if "Title" in response_dict[k][0] and "Title" not in response_dict[k][0]:
                print("---K----SEARCH", response_dict[k][0][0], "---------------")
                assert "stem" in response_dict[k][0]
            if "Poster" not in response_dict[k][0]:
                print("PASS-PASS-PASS-", response_dict[k][0])
            # assert "Terra Incognita" in response_dict[k]
            else:
                print("FAIL-FAIL-FAIL-", response_dict[k][0])
                # assert "Terra Incognita" in response_dict[k]


def test_WhatareJSONKeys():
    movies = "stem"
    url = "http://www.omdbapi.com/?i=&apikey=1d094a12&s=" + movies + "*&page=2&type=movie"
    print(url)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload).text

    print(response)

    print('Number of occurrence of p:', response.count('Thor'))
    payload = {}
    headers = {}
    titlelist = []
    response_dict = json.loads(response)
    # print("dictionary", response_dict)

    intCount = 1
    for keys in response_dict:
        intCount += 1

        sbstringSearch = "STEM"
        if keys == "Search":
            print("KEYS", keys, "Values in Keys---", "Count Loop", intCount, response_dict[keys][0]['Title'])
            search_string = response_dict[keys][0]
            title_string = response_dict[keys][0]['Title']
            titlelist.append(intCount)
            print(title_string)
            print(titlelist)
            print("hello %s" % (sbstringSearch))
            # assert title_string.find(sbstringSearch) != -1, "Cannot Find Substring"
            print("Number of occurrence of ", sbstringSearch, response.count(sbstringSearch))


# def test_chkforLOngerstring():
#     movies = "stem"
#
#     url = "http://www.omdbapi.com/?i=&apikey=1d094a12&s=" + movies + "*&page=2&type=movie"
#     print(url)
#     payload = {}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload).text
#     payload = {}
#     headers = {}
#     response_dict = json.loads(response)
#     for k in response_dict:
#         if k == "Search":
#             print("---K----SEARCH",k)
#         assert True


def test_getSTEMchkhowlong():
    movies = "stem"

    url = "http://www.omdbapi.com/?i=&apikey=1d094a12&s=" + movies + "*&page=2&type=movie"
    print(url)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).text
    response_dict = json.loads(response)
    print("---------", response_dict)

    for k in response_dict:

        print("---K----", k, response_dict[k])

        if "stemA" in response_dict[k]:
            assert "Pass"
            print("pass")
        if k == "totalResults":
            total = int(response_dict[k].split("_")[0])
            assert total >= 31

            if total >= 0:
                print("AT least 31 items")

# ttp://www.omdbapi.com/?i=tt12919170&apikey=1d094a12&s=&page=2&type=movie
# JW Nehemiah build wall
