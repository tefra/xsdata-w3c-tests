from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo1"


@dataclass
class Foo1:
    """
    :ivar any_element:
    :ivar x:
    """
    class Meta:
        name = "foo1"
        namespace = "foo1"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    x: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
