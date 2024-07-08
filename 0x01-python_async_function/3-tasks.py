#!/usr/bin/env python3
"""
3_tasks module
"""

import asyncio
from _0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random coroutine.
    
    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
