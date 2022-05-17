
# Import packages

import glob

import gzip

import logging

import shutil

from datetime import date, timedelta

import requests

from bs4 import BeautifulSoup

import re

import os

API_KEY = "202001ZjMvj8R3BF"

s = requests.Session()


def get_urls(url: str, urls=None) -> list:
    global s
    # Last Modified 1-Aban-1400

    try:

        # Package the request, send the request and catch the response: r

        r = s.get(url)

        # Extracts the response as html: page

        page = r.text

        # create a BeautifulSoup object from the HTML: soup

        soup = BeautifulSoup(page, features="html.parser")

        # Find all 'a' tags (which define hyperlinks) ends with .tsv.gz: a_tags

        a_tags = soup.find_all('a', {'href': re.compile(r'tsv.gz$')})

        # iterate over ResultSet and list all the urls

        urls = list(map(lambda x: url + x.get('href'), a_tags))

        return urls

    except Exception as e:
        print("here 0")
        logging.error(e)


def populate_zip_dir(urls: list, dir: str) -> None:
    global s
    # Last Modified 1-Aban-1400

    try:

        for url in urls[::-1]:

            # Create the filename

            filename = url.split("/")[-1]

            # Set the path for our files

            filepath = os.path.join(
                os.getcwd(), 'BTC', 'Data', 'ZIP', dir, filename)

            if os.path.exists(filepath) and os.path.getsize(filepath) != 0:
                logging.warning(
                    f"I've already downloaded the file {filename}!")

            else:
                with open(filepath, "wb") as f:
                    r = s.get(f"{url}?key={API_KEY}")

                    f.write(r.content)

    except Exception as e:

        logging.error(e)


def populate_csv_dir(files: list) -> None:

    try:

        for f in files:

            print(f)

            filename = f.replace('tsv.gz', 'tsv').replace('ZIP', 'CSV')

            print(filename)

            if os.path.exists(filename) and os.path.getsize(filename) != 0:

                logging.warning(f"I've already extracted the file {filename}!")

            else:

                with gzip.open(f, 'rb') as f_in:

                    with open(filename, 'wb') as f_out:

                        shutil.copyfileobj(f_in, f_out)

    except Exception as e:
        print("here 2")

        logging.error(e)


if __name__ == "__main__":

    # Specify url

    # url = 'https://gz.blockchair.com/bitcoin/transactions/'

    # url = 'https://gz.blockchair.com/bitcoin/blocks/'

    # url = 'https://gz.blockchair.com/bitcoin/inputs/'

    url = 'https://gz.blockchair.com/bitcoin/outputs/'

    # get the name of new directory to store compressed files

    new_dir = url.rsplit('/')[-2]

    dirpath = os.path.join(os.getcwd(), 'BTC', 'Data', 'ZIP', new_dir)

    try:

        if not os.path.exists(dirpath):

            os.makedirs(dirpath)

    except Exception as e:

        logging.error(e)

    # extract desired urls

    urls = get_urls(url)

    # populate Data/ZIP/new_dir directory

    populate_zip_dir(urls, new_dir)

    # list all the zip files

    # zip_files = glob.glob(f'BTC/Data/**/{new_dir}/*.tsv.gz')

    # # extract zip files in CSV dir

    # dirpath = os.path.join(os.getcwd(), 'BTC', 'Data', 'CSV', new_dir)

    # try:

    #     if not os.path.exists(dirpath):

    #         os.makedirs(dirpath)

    # except Exception as e:

    #     logging.error(e)


# PA__L5085fFz9dZlrvsqoW1kKTM4EtE9

# curl https://gz.blockchair.com/bitcoin/outputs/blockchair_bitcoin_outputs_20130328.tsv.gz?key=SECRETKEY
