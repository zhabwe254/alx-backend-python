#!/usr/bin/env python3
import asyncio
from typing import List

from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the list of delays.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
