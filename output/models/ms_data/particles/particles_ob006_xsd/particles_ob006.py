from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar any_element:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )


@dataclass
class R(B):
    """
    :ivar foo_bar_element:
    """
    foo_bar_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="foo bar"
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