from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://simple022.ly/"


class PriceValue(Enum):
    VALUE_9_99 = 9.99
    NA_N = float("nan")


@dataclass(kw_only=True)
class Price:
    class Meta:
        name = "price"
        namespace = "http://simple022.ly/"

    value: PriceValue = field()
