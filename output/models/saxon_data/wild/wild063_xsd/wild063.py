from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class E:
    class Meta:
        name = "e"

    value: int = field()


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    e: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    f: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    local_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class Doc(Zing):
    class Meta:
        name = "doc"
