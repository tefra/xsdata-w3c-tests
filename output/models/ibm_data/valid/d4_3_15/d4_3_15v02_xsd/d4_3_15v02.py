from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ArrayType:
    """
    :ivar ele:
    :ivar length:
    """
    class Meta:
        name = "arrayType"

    ele: List[str] = field(
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
class Root(ArrayType):
    class Meta:
        name = "root"
