from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class E:
    """
    :ivar any_element:
    """
    class Meta:
        name = "e"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class E1:
    """
    :ivar value:
    """
    class Meta:
        name = "e1"
        namespace = "foo"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar e1:
    :ivar e:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    e1: Optional[E1] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    e: Optional[E] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
