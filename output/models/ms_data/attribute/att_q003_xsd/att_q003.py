from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Elem:
    """
    :ivar att1:
    :ivar att2:
    :ivar att3:
    """
    class Meta:
        name = "elem"
        namespace = "http://xsdtesting"

    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    att3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
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

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
