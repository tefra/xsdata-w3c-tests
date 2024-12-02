from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "IdConstrDefs/fields"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/fields"

    number: list[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
