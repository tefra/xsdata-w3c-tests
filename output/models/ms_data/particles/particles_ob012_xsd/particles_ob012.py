from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar other_element:
    """
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other"
        )
    )


@dataclass
class R:
    """
    :ivar other_element:
    """
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
