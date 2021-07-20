from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Global:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: Optional[bool] = field(
        default=None
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    global_value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Global",
            "type": "Element",
        }
    )
    local: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
