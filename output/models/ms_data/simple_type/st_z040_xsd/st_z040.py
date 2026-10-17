from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import StrEnum

__NAMESPACE__ = "urn:test"


class Myunion2Value(StrEnum):
    A = "a"
    B = "b"


@dataclass(kw_only=True)
class Info2:
    class Meta:
        name = "info2"
        namespace = "urn:test"

    value: Decimal | Myunion2Value = field()
