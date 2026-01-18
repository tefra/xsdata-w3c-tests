from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class BaseType:
    class Meta:
        name = "baseType"

    base_ely: list[object] = field(
        default_factory=list,
        metadata={
            "name": "baseEly",
            "type": "Element",
            "namespace": "",
        },
    )
    base_attr: None | str = field(
        default=None,
        metadata={
            "name": "baseAttr",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DerivedType(BaseType):
    class Meta:
        name = "derivedType"

    derived_attr: None | str = field(
        default=None,
        metadata={
            "name": "derivedAttr",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(DerivedType):
    class Meta:
        name = "root"
