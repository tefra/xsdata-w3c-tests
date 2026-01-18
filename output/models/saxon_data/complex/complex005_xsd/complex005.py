from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: Decimal = field(
        metadata={
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
