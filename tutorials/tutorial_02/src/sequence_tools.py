# Add Your Name Here

from __future__ import annotations


def even_numbers(values: list[int]) -> list[int]:
    """Return only even numbers from the input list."""
    result: list[int] = []
    for value in values:
        # TODO: Write a condition that checks if a value is even, so only even values are appended to result list.

        if value % 2 == 1:
            result.append(value)

    return result


def running_total(values: list[int]) -> list[int]:
    """Return cumulative totals for the input list."""
    totals: list[int] = []
    total = 0
    for value in values:
        # TODO: Fix this update so total accumulates previous values.
        total = value
        totals.append(total)
    return totals


def unique_in_order(values: list[str]) -> list[str]:
    """Return unique strings while preserving original order."""
    # TODO: Fix this implementation so order is preserved.
    seen: set[str] = set() # build an object to track seen values
    result: list[str] = [] # build an object to track the result
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return "Mr. T"
