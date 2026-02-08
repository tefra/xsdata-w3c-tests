from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "A"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class A2:
    class Meta:
        name = "a"

    value: str = field(default="")


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
    a_or_a: None | A1 | A2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "A",
                    "type": A1,
                },
                {
                    "name": "a",
                    "type": A2,
                },
            ),
        },
    )
    b: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Root(Zing):
    class Meta:
        name = "root"
