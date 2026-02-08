from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Type1:
    class Meta:
        name = "type1"

    local: bool = field(
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Type2:
    class Meta:
        name = "type2"

    local: Decimal = field(
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        }
    )
