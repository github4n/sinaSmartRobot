#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018 Oct 12 
# @Author  : WangSai
import random
import time


def getRandomNumBetween60And1400():
    return int(time.time() * 1000) % 1000 + random.randint(60, 400)

if __name__ == "__main__":
    print(random.randrange(5, 70) / 10)
    print(int(time.time() * 1000) % 1000 + random.randint(60, 400))
    print(getRandomNumBetween60And1400())


