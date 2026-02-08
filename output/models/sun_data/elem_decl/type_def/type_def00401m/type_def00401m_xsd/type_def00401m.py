from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Global:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: bool = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    global_value: Global = field(
        metadata={
            "name": "Global",
            "type": "Element",
        }
    )
    local: Decimal = field(
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        }
    )
