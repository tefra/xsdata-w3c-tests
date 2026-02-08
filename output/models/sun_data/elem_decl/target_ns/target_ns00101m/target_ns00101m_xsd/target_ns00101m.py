from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "ElemDecl/targetNS"


@dataclass(kw_only=True)
class Number:
    class Meta:
        name = "number"
        namespace = "ElemDecl/targetNS"

    value: Decimal = field()
