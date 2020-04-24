from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    """
    :ivar other_element:
    """
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            required=True
        )
    )


@dataclass
class Date:
    """
    :ivar value:
    """
    class Meta:
        name = "date"
        namespace = "nsConstraint"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
