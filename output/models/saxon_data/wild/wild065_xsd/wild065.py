from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class E:
    class Meta:
        name = "e"

    value: Decimal = field()


@dataclass(kw_only=True)
class G:
    class Meta:
        name = "g"

    value: int = field()


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    g_or_e: None | G | E = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g",
                    "type": G,
                },
                {
                    "name": "e",
                    "type": E,
                },
            ),
        },
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
