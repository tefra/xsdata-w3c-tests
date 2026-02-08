from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: Decimal = field()
