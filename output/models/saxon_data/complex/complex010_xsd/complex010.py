from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: Decimal = field()
    no_namespace_schema_location: str = field(
        metadata={
            "name": "noNamespaceSchemaLocation",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        }
    )
