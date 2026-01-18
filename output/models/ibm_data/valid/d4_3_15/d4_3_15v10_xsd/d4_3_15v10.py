from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class BaseType:
    class Meta:
        name = "baseType"

    base_element: list[object] = field(
        default_factory=list,
        metadata={
            "name": "baseElement",
            "type": "Element",
            "namespace": "",
        },
    )
    attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DerivedType(BaseType):
    class Meta:
        name = "derivedType"


@dataclass(kw_only=True)
class Root(DerivedType):
    class Meta:
        name = "root"
