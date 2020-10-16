from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar s1:
    :ivar s2:
    :ivar s3:
    :ivar s4:
    :ivar n1_element:
    :ivar n2_element:
    :ivar n3_element:
    :ivar n4_element:
    """
    class Meta:
        name = "foo"

    s1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    s2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    s3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    s4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    n1_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://n1",
        }
    )
    n2_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://n2",
        }
    )
    n3_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://n3",
        }
    )
    n4_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://n4",
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
