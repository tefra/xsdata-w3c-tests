from dataclasses import dataclass, field
from typing import Optional


@dataclass
class R:
    """
    :ivar www_target001_com_element:
    :ivar child:
    """
    www_target001_com_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://www.target001.com/",
            required=True
        )
    )
    child: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.target001.com/",
            required=True
        )
    )


@dataclass
class Parent(R):
    class Meta:
        name = "parent"
