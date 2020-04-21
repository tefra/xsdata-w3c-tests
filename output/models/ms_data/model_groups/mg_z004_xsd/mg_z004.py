from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:test"


@dataclass
class Root:
    """
    :ivar content:
    :ivar a:
    :ivar b1:
    :ivar b2:
    :ivar b3:
    :ivar b4:
    :ivar b5:
    """
    class Meta:
        namespace = "urn:test"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    a: Optional[str] = field(
        default=None,
        metadata=dict(
            name="A",
            type="Element",
            required=True
        )
    )
    b1: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="B1",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    b2: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="B2",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    b3: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="B3",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    b4: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="B4",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    b5: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="B5",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
