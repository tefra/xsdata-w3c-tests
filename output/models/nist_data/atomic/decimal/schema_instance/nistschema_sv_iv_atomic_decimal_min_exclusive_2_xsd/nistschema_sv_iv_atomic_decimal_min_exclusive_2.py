from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-2-NS"

    value: Decimal = field(
        metadata={
            "min_exclusive": Decimal("631308414640570968"),
        }
    )
