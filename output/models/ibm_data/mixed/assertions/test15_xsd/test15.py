from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class XType:
    """
    :ivar value:
    :ivar a:
    """
    class Meta:
        name = "x_Type"

    value: Optional[int] = field(
        default=None,
    )
    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True,
            max_length=20,
            pattern=r"val[1-9][0-9]*"
        )
    )


@dataclass
class Example:
    """
    :ivar x:
    :ivar x_count:
    """
    x: List[XType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    x_count: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
