#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

#python3.5 为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程

# async def downloader(url):
#     return "bobby"

@types.coroutine
def downloader(url):
    yield "bobby"

async def download_url(url):
    #dosomethings
    html = await downloader(url)
    return html

if __name__ == "__main__":
    coro = download_url("http://www.imooc.com")
    # next(None)
    print(coro.send(None))











