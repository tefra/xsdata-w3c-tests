from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar choice:
    """
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "d1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "d2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 100,
        }
    )


@dataclass
class R(B):
    """
    :ivar c1:
    """
    c1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 30,
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
