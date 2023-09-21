#! /usr/bin/python

import os
import requests
import subprocess
from random import randint
from bs4 import BeautifulSoup
from pathlib import Path
from argparse import ArgumentParser


user_agents = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
    "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17",
    "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",
    "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
]


def main(domains, filetype, page_count, outputdir, download):
    if page_count is True:
        page_count = 3

    if outputdir:
        if not os.path.exists("data"):
            os.mkdir("data")

    for domain in domains:
        for page_nr in range(1, int(page_count)):
            url = "https://www.startpage.com/sp/search"
            agent = user_agents[randint(0, len(user_agents) - 1)]
            payload = {
                "query": f"filetype:{filetype} site:{domain}",
                "t": "",
                "lui": "english",
                "sc": "8MFHHLOzriFE20",
                "cat": "web",
                "page": page_nr
            }

            r = requests.post(
                url=url, headers={"User-Agent": agent}, data=payload)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            anchs = soup.find_all("a")

            # Find links
            for link in anchs:
                link_url = link.get("href")

                # print(page_nr)
                #  and "/do/settings?query=" not in link_url
                if domain in link_url and not link_url.startswith("/do/settings"):
                    print(link_url)

                    if not outputdir:
                        continue

                    # Make dir
                    split = link_url.split(f"{domain}/")
                    file = split[1]
                    file = f"{outputdir}/{domain}/{file}"

                    if not os.path.exists(file):
                        if download:
                            # Download
                            filepath = Path(file).parent
                            subprocess.call(["mkdir", "-p", filepath])
                            r = requests.get(link_url, allow_redirects=True)
                            with open(file, 'wb') as f:
                                f.write(r.content)
                        else:
                            # Just store the link file
                            subprocess.call(["mkdir", "-p", file])
                            with open(f"{file}/link.txt", "w") as f:
                                f.write(link_url)


if __name__ == "__main__":

    banner = """
 _       _       _ _ _  __ _           _ 
(_)     | |     | | (_)/ _(_)         | |
 _ _ __ | |_ ___| | |_| |_ _ _ __   __| |
| | '_ \| __/ _ \ | | |  _| | '_ \ / _` |
| | | | | ||  __/ | | | | | | | | | (_| |
|_|_| |_|\__\___|_|_|_|_| |_|_| |_|\__,_|
                                        
                                        

Find files the intelligent way.

Uses startpage as a google proxy to search for files on domains.
Queries like filetype:<type> site:<domain>
"""

    print(banner)

    parser = ArgumentParser(prog="intellifind")
    parser.add_argument("domains")
    parser.add_argument("-f", "--filetype", default="pdf")
    parser.add_argument("-c", "--count", default=3)
    parser.add_argument("-o", "--outputdir", default=False)
    parser.add_argument("-d", "--download",
                        action="store_true", default=False)
    args = parser.parse_args()

    domains = args.domains.split(",")
    filetype = args.filetype
    count = args.count
    outputdir = args.outputdir
    download = args.download

    if download and not outputdir:
        print("Specify outputdir. Example -o ./data")
        exit(1)

    main(domains, filetype, count, outputdir, download)
