from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"

    value: str = field(default="")
    att1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AnyType:
    class Meta:
        name = "any"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    any_or_a: list[AnyType | A] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "any",
                    "type": AnyType,
                },
                {
                    "name": "a",
                    "type": A,
                },
            ),
        },
    )
