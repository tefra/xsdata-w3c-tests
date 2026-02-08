from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Att1:
    class Meta:
        name = "att1"

    att: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Att2:
    class Meta:
        name = "att2"

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
class E1:
    class Meta:
        name = "e1"

    value: str = field(
        default="",
        metadata={
            "length": 4,
        },
    )


@dataclass(kw_only=True)
class M3:
    class Meta:
        name = "m3"

    e31: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
        },
    )
    att: int = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class M6:
    class Meta:
        name = "m6"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class E2(Att1):
    class Meta:
        name = "e2"


@dataclass(kw_only=True)
class E3(M3):
    class Meta:
        name = "e3"


@dataclass(kw_only=True)
class E6(M6):
    class Meta:
        name = "e6"


@dataclass(kw_only=True)
class E7(Att1):
    class Meta:
        name = "e7"


@dataclass(kw_only=True)
class E8(Att1):
    class Meta:
        name = "e8"


@dataclass(kw_only=True)
class M4:
    class Meta:
        name = "m4"

    e41: list[Att2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
            "sequence": 1,
        },
    )
    e3: list[E3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequence": 1,
        },
    )
    att: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class E4(M4):
    class Meta:
        name = "e4"


@dataclass(kw_only=True)
class M5:
    class Meta:
        name = "m5"

    e3_or_e4_or_e5: list[E3 | E4 | E5] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e3",
                    "type": E3,
                },
                {
                    "name": "e4",
                    "type": E4,
                },
                {
                    "name": "e5",
                    "type": ForwardRef("E5"),
                },
            ),
        },
    )
    att: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class E5(M5):
    class Meta:
        name = "e5"


@dataclass(kw_only=True)
class Ct1:
    class Meta:
        name = "ct1"

    e1: None | E1 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    e2: None | E2 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    e3: list[E3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    e4: list[E4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    e5: list[E5] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    e6: list[E6] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    e7: list[E7] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    e8: list[E8] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Root(Ct1):
    class Meta:
        name = "root"
