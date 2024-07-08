#!/usr/bin/env python3
"""
4_tasks module
"""

import asyncio
from typing import List
from _3_tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    
    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
