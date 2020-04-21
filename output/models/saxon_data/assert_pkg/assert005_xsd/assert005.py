from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Inner:
    """
    :ivar a:
    :ivar x:
    :ivar y:
    """
    class Meta:
        name = "inner"

    a: List["Inner.A"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=4
        )
    )
    x: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    y: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    @dataclass
    class A:
        """
        :ivar b:
        """
        b: List[object] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                min_occurs=0,
                max_occurs=4
            )
        )


@dataclass
class Outer:
    """
    :ivar inner:
    """
    class Meta:
        name = "outer"

    inner: List[Inner] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
