from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    """
    :ivar att:
    :ivar att1:
    :ivar att2:
    """
    class Meta:
        name = "attRef"

    att: int = field(
        init=False,
        default=37,
        metadata={
            "type": "Attribute",
        }
    )
    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
