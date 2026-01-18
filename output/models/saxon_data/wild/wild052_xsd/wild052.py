from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Zang:
    class Meta:
        name = "zang"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
