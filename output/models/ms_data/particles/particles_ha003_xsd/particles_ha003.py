from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar e1:
    :ivar e2_or_e3:
    """
    class Meta:
        name = "base"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    e2_or_e3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e3",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 2,
        }
    )


@dataclass
class Doc:
    """
    :ivar e1:
    :ivar e2_or_e3:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    e2_or_e3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e2",
                    "type": object,
                },
                {
                    "name": "e3",
                    "type": object,
                },
            ),
            "max_occurs": 2,
        }
    )
