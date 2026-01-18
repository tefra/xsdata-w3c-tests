from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-length-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDecimalLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-length-1"
        namespace = "NISTSchema-SV-IV-list-decimal-length-1-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
