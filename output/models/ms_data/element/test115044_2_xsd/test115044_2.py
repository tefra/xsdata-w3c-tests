from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class E:
    class Meta:
        name = "e"
        namespace = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class E1:
    class Meta:
        name = "e1"
        namespace = "foo"

    value: int = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    e1_or_e: None | E1 | E = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": E1,
                },
                {
                    "name": "e",
                    "type": E,
                },
            ),
        },
    )
