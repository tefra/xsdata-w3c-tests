from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Ct1:
    """
    :ivar any_element:
    :ivar element1:
    """
    class Meta:
        name = "ct1"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
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
    """
    :ivar element1:
    :ivar any_element:
    """
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
            "required": True,
        }
    )


@dataclass
class Ct3:
    """
    :ivar element1:
    :ivar any_element:
    """
    class Meta:
        name = "ct3"

    element1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Ct4:
    """
    :ivar any_element:
    :ivar element1:
    """
    class Meta:
        name = "ct4"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "min_occurs": 1,
            "max_occurs": 2,
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
class Ct5:
    """
    :ivar element1:
    :ivar any_element:
    """
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
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )


@dataclass
class Ct6:
    """
    :ivar element1:
    :ivar any_element:
    """
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
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class Element1:
    """
    :ivar any_element:
    """
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
    """
    :ivar any_element:
    """
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
    """
    :ivar any_element:
    """
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
    """
    :ivar e1:
    :ivar e2:
    :ivar e3:
    :ivar e4:
    :ivar e5:
    :ivar e6:
    """
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
