from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Keyname:
    class Meta:
        name = "keyname"

    numid: int = field(
        metadata={
            "name": "Numid",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    numname: str = field(
        metadata={
            "name": "Numname",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    number: list[Keyname] = field(
        default_factory=list,
        metadata={
            "name": "Number",
            "type": "Element",
            "min_occurs": 1,
        },
    )
