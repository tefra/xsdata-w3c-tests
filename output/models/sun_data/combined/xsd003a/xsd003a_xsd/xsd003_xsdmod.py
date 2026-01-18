from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class ComplexType:
    class Meta:
        name = "complexType"

    root: list[Root] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    g_att: None | str = field(
        default=None,
        metadata={
            "name": "gAtt",
            "type": "Attribute",
            "namespace": "foo",
        },
    )


@dataclass(kw_only=True)
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "foo"
