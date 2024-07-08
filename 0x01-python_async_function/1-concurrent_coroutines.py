#!/usr/bin/env python3

import asyncio
from 1-concurrent_coroutines import wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
