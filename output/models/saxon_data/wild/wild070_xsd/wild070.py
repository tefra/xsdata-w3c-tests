from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    a: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    c: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class Root(Zing):
    class Meta:
        name = "root"
