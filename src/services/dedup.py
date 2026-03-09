"""Simple de-duplication utilities.

The main goal here is to have something deterministic and testable.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable, List, Sequence, Tuple, TypeVar


T = TypeVar("T")


@dataclass(frozen=True)
class DedupResult:
    """Result of a dedup operation."""

    unique: Tuple[T, ...]
    duplicates: Tuple[T, ...]


def dedup_keep_order(items: Iterable[T]) -> DedupResult:
    """Return items without duplicates while preserving first-seen order.

    Parameters
    ----------
    items:
        An iterable of hashable items.

    Returns
    -------
    DedupResult
        unique: items with duplicates removed (first occurrence kept)
        duplicates: items that were seen more than once (in encounter order)
    """

    seen: set[Hashable] = set()
    unique: List[T] = []
    duplicates: List[T] = []
    for item in items:
        # Runtime enforcement: most callers will pass hashables; if not,
        # Python raises TypeError and tests will catch it.
        if item in seen:  # type: ignore[operator]
            duplicates.append(item)
            continue
        seen.add(item)  # type: ignore[arg-type]
        unique.append(item)
    return DedupResult(unique=tuple(unique), duplicates=tuple(duplicates))


def chunked(seq: Sequence[T], size: int) -> List[List[T]]:
    """Split a sequence into chunks of a given size.

    Raises
    ------
    ValueError
        If size <= 0.
    """

    if size <= 0:
        raise ValueError("size must be > 0")
    return [list(seq[i : i + size]) for i in range(0, len(seq), size)]
