from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Ct1:
    class Meta:
        name = "ct1"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    element1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Ct2:
    class Meta:
        name = "ct2"

    element1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Ct3:
    class Meta:
        name = "ct3"

    element1_or_any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "element1",
                    "type": object,
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##any",
                },
            ),
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )


@dataclass
class Ct4:
    class Meta:
        name = "ct4"

    any_element_or_element1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##any",
                },
                {
                    "name": "element1",
                    "type": object,
                },
            ),
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )


@dataclass
class Ct5:
    class Meta:
        name = "ct5"

    element1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 3,
        }
    )


@dataclass
class Ct6:
    class Meta:
        name = "ct6"

    element1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 2,
        }
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
            "required": True,
        }
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
            "required": True,
        }
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
            "required": True,
        }
    )


@dataclass
class Test:
    class Meta:
        name = "test"

    e1: List[Ct1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    e2: List[Ct2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    e3: List[Ct3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    e4: List[Ct4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    e5: List[Ct5] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    e6: List[Ct6] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
