from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar open_com_element:
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "doc"

    open_com_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://open.com/",
            required=True
        )
    )
    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    c: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )