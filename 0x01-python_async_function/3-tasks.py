#!/usr/bin/env python3
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return a asyncio.Task that waits for a random delay between 0 and max_delay seconds.
    """
    return asyncio.create_task(wait_random(max_delay))
