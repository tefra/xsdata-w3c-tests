from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union


@dataclass
class E:
    class Meta:
        name = "e"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class G:
    class Meta:
        name = "g"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    g_or_e: Optional[Union[G, E]] = field(
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
    f: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        },
    )


@dataclass
class Doc(Zing):
    class Meta:
        name = "doc"
