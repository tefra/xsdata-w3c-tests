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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    length: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Xlist(ArrayType):
    class Meta:
        name = "XList"
