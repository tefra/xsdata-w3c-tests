from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar any_element:
    :ivar e2:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    e2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class R:
    """
    :ivar any_element:
    :ivar e1:
    :ivar e2:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    e1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    e2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
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