from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Triangular:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar kind:
    """
    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    c: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    kind: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class Quadrilateral(Triangular):
    """
    :ivar d:
    """
    d: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Shapes:
    """
    :ivar polygon:
    """
    class Meta:
        name = "shapes"

    polygon: List[Union[Quadrilateral, Triangular]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
