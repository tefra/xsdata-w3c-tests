from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Att1:
    class Meta:
        name = "att1"

    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Att2:
    class Meta:
        name = "att2"

    att1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class E1:
    class Meta:
        name = "e1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 4,
        },
    )


@dataclass
class M3:
    class Meta:
        name = "m3"

    e31: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
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
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class E2(Att1):
    class Meta:
        name = "e2"


@dataclass
class E3(M3):
    class Meta:
        name = "e3"


@dataclass
class E6(M6):
    class Meta:
        name = "e6"


@dataclass
class E7(Att1):
    class Meta:
        name = "e7"


@dataclass
class E8(Att1):
    class Meta:
        name = "e8"


@dataclass
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
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class E4(M4):
    class Meta:
        name = "e4"


@dataclass
class M5:
    class Meta:
        name = "m5"

    e3_or_e4_or_e5: list[Union[E3, E4, "E5"]] = field(
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
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class E5(M5):
    class Meta:
        name = "e5"


@dataclass
class Ct1:
    class Meta:
        name = "ct1"

    e1: Optional[E1] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    e2: Optional[E2] = field(
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


@dataclass
class Root(Ct1):
    class Meta:
        name = "root"
