#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

#webscraper to get the most recent release.
#Preferring this method over https://s3.amazonaws.com/dstbuilds/builds.json as builds.json often contains releases that aren't actually fully released yet.

URL="https://forums.kleientertainment.com/game-updates/dst/"

def get_latest_version():
    releases=[]
    r = requests.get(URL)
    soup=BeautifulSoup(r.content,"html.parser")
    releases_html=soup.find_all("a", {"class": "cRelease"})
    for release_a in releases_html:
        release_link=release_a.get("href")
        release_number=release_link[release_link.index("/dst/")+len("/dst/"):release_link.index("-r")]
        releases.append(release_number)
    return releases[0]




if __name__ == "__main__":
    import pprint
    latest=get_latest_version()
    print(latest)
