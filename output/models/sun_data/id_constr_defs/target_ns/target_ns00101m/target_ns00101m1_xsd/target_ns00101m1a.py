from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "IdConstrDefs/targetNSa"


@dataclass(kw_only=True)
class Roota:
    class Meta:
        name = "roota"
        namespace = "IdConstrDefs/targetNSa"

    person: list[Roota.Person] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Person:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        parent: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
