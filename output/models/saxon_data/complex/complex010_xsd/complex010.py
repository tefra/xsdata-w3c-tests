from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar value:
    :ivar no_namespace_schema_location:
    """
    class Meta:
        name = "root"

    value: Optional[Decimal] = field(
        default=None,
    )
    no_namespace_schema_location: Optional[str] = field(
        default=None,
        metadata=dict(
            name="noNamespaceSchemaLocation",
            type="Attribute",
            namespace="http://www.w3.org/2001/XMLSchema-instance",
            required=True
        )
    )