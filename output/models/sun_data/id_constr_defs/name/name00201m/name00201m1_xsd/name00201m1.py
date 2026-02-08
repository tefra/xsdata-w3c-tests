from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "IdConstrDefs/name"


@dataclass(kw_only=True)
class Name:
    class Meta:
        name = "name"
        namespace = "IdConstrDefs/name"

    name: list[Name.NameInner] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class NameInner:
        value: str = field(default="")
        name: None | object = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
