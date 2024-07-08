#!/usr/bin/env python3
"""
2_measure_runtime module
"""

import time
import asyncio
from _1_concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n and returns total_time / n.
    
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: Average execution time per wait_random call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
