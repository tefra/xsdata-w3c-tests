from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Decimal] = field(
        default=None,
    )
    no_namespace_schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "noNamespaceSchemaLocation",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        }
    )
