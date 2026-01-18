from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrUse/valConstr"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrUse/valConstr"

    number: int = field(
        init=False,
        default=12,
        metadata={
            "type": "Attribute",
            "namespace": "AttrUse/valConstr",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrUse/valConstr"

    element_with_attr: ElementWithAttr = field(
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
            "required": True,
        }
    )
