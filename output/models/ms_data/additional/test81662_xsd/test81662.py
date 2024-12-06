from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Ct1:
    class Meta:
        name = "ct1"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    element1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Ct2:
    class Meta:
        name = "ct2"

    element1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Ct3:
    class Meta:
        name = "ct3"

    element1_or_any_element: list[Union["Ct3.Element1", object]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "element1",
                    "type": ForwardRef("Ct3.Element1"),
                    "max_occurs": 2,
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##any",
                },
            ),
            "min_occurs": 2,
            "max_occurs": 3,
        },
    )

    @dataclass
    class Element1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )


@dataclass
class Ct4:
    class Meta:
        name = "ct4"

    any_element_or_element1: list[Union["Ct4.Element1", object]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "element1",
                    "type": ForwardRef("Ct4.Element1"),
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##any",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass
    class Element1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )


@dataclass
class Ct5:
    class Meta:
        name = "ct5"

    element1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 3,
        },
    )


@dataclass
class Ct6:
    class Meta:
        name = "ct6"

    element1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 2,
        },
    )


@dataclass
class Element1:
    class Meta:
        name = "element1"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Element2:
    class Meta:
        name = "element2"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Element3:
    class Meta:
        name = "element3"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Test:
    class Meta:
        name = "test"

    e1: list[Ct1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    e2: list[Ct2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    e3: list[Ct3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    e4: list[Ct4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    e5: list[Ct5] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    e6: list[Ct6] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
