from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar annotation:
    :ivar element_or_any:
    """
    annotation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    element_or_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "element",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "any",
                    "type": object,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class Derived:
    """
    :ivar annotation:
    :ivar element_or_any:
    :ivar element:
    """
    annotation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    element_or_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "element",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "any",
                    "type": object,
                    "namespace": "",
                },
            ),
        }
    )
    element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
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

    elem: Optional[Derived] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
