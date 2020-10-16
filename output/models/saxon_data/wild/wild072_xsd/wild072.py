from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A2:
    """
    :ivar any_element:
    """
    class Meta:
        name = "A"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class A1:
    """
    :ivar value:
    """
    class Meta:
        name = "a"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Zing:
    """
    :ivar a_element:
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar any_element:
    """
    class Meta:
        name = "zing"

    a_element: Optional[A2] = field(
        default=None,
        metadata={
            "name": "A",
            "type": "Element",
        }
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
