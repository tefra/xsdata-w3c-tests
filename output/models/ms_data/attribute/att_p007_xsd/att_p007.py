from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    """
    :ivar att:
    """
    class Meta:
        name = "attRef"

    att: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
            "required": True,
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

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
