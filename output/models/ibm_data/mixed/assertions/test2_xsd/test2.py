from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ArrayType:
    """
    :ivar entry:
    :ivar length:
    """
    entry: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Xlist(ArrayType):
    class Meta:
        name = "XList"
