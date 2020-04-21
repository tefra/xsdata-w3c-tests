from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-b"


@dataclass
class FooB:
    """
    :ivar any_element:
    """
    class Meta:
        name = "foo_b"
        namespace = "ns-b"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
