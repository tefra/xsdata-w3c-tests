from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    """
    :ivar z:
    :ivar any_element:
    """
    class Meta:
        name = "t"

    z: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="a"
        )
    )
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Z:
    """
    :ivar value:
    """
    class Meta:
        name = "z"
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
