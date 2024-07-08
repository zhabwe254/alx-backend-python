#!/usr/bin/env python3

import asyncio
from 0-basic_async_syntax import wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
