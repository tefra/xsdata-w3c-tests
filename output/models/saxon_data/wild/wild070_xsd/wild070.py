from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Zing:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar any_element:
    """
    class Meta:
        name = "zing"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"