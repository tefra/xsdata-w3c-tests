from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class ACt:
    """
    :ivar att1:
    :ivar att2:
    :ivar att3:
    :ivar att5:
    :ivar att6:
    :ivar att7:
    :ivar att9:
    :ivar att11:
    :ivar att12:
    :ivar att13:
    :ivar att14:
    :ivar att15:
    :ivar att16:
    """
    class Meta:
        name = "A-ct"

    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att3: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    att5: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att6: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att7: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    att9: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    att11: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            total_digits=1
        )
    )
    att12: str = field(
        default="abc",
        metadata=dict(
            type="Attribute"
        )
    )
    att13: str = field(
        init=False,
        default="fix",
        metadata=dict(
            type="Attribute"
        )
    )
    att14: str = field(
        default="abc",
        metadata=dict(
            type="Attribute"
        )
    )
    att15: str = field(
        init=False,
        default="fix",
        metadata=dict(
            type="Attribute"
        )
    )
    att16: str = field(
        init=False,
        default="fix",
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class E2:
    """
    :ivar value:
    """
    class Meta:
        name = "e2"
        namespace = "ns-a"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            total_digits=2
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class E1(ACt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
