#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip install aiohttp
pip install aiomysql
pip install pyquery
"""
import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery

start_url = "https://jobbole.iteye.com/"
waitting_urls = []
seen_urls = set()
stopping = False


async def fetch(url, session):
    try:
        async with session.get(url) as resp:
            print(f"url status: {resp.status}")
            if resp.status in [200, 201]:
                data = await resp.text()
                return data
    except Exception as e:
        print(e)

def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        url = "".join(url)
        if url and url.startwith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls

async def init_urls(url, session):
    html = await fetch(url,session)
    extract_urls(html)

async def article_handler(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    print(f"结果：{title}")


async def consumer():
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waitting_urls.pop()
            print(f"start get url: {url}")
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session))

async def main(loop):
    # pool = await aiomysql.create_pool(host="127.0.0.1", port=3306,
    #                 user="root", password="poly2017", db="cpq", loop=loop,
    #                 charset="utf8", autocommit=True)
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)

    asyncio.ensure_future(consumer())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
















