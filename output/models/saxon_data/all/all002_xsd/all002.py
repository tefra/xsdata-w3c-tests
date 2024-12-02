from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class C1:
    class Meta:
        name = "C"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class D1:
    class Meta:
        name = "D"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class C2:
    class Meta:
        name = "c"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class D2:
    class Meta:
        name = "d"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    a: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    b: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    c_or_c: list[Union[C1, C2]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "C",
                    "type": C1,
                },
                {
                    "name": "c",
                    "type": C2,
                },
            ),
        },
    )
    d_or_d: Optional[Union[D1, D2]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "D",
                    "type": D1,
                },
                {
                    "name": "d",
                    "type": D2,
                },
            ),
        },
    )
