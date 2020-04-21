from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    """
    :ivar any_element:
    """
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
