from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    value: Decimal = field(
        default=Decimal("12"),
        metadata={
            "required": True,
        }
    )
