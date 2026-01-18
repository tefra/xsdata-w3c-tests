from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-length-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDecimalLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-length-3"
        namespace = "NISTSchema-SV-IV-list-decimal-length-3-NS"

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
