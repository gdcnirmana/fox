"""A tiny in-memory worker queue.

Note: the filename is kept as `woker.py` to match the existing repo layout.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable, Deque, Generic, Optional, TypeVar


T = TypeVar("T")


@dataclass(frozen=True)
class Job(Generic[T]):
    id: str
    payload: T


class InMemoryWorker(Generic[T]):
    """A minimal FIFO worker.

    Designed for easy unit testing.
    """

    def __init__(self) -> None:
        self._queue: Deque[Job[T]] = deque()

    def enqueue(self, job: Job[T]) -> None:
        self._queue.append(job)

    def size(self) -> int:
        return len(self._queue)

    def pop(self) -> Optional[Job[T]]:
        if not self._queue:
            return None
        return self._queue.popleft()

    def drain(self, handler: Callable[[Job[T]], None]) -> int:
        """Process all queued jobs with handler.

        Returns number of processed jobs.
        """

        processed = 0
        while True:
            job = self.pop()
            if job is None:
                break
            handler(job)
            processed += 1
        return processed
