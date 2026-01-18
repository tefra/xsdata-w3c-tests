from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class E2:
    class Meta:
        name = "e2"
        nillable = True

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "e3",
                    "type": int,
                    "namespace": "",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    e1: str = field(
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
    e2: None | E2 = field(
        metadata={
            "type": "Element",
            "nillable": True,
        }
    )
