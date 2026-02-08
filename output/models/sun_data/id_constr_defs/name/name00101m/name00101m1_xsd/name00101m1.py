from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "IdConstrDefs/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/name"

    person: list[Root.Person] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Person:
        value: str = field(default="")
        parent: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
