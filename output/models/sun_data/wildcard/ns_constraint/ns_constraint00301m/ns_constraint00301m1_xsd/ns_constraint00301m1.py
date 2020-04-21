from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    """
    :ivar ns_test1_ns_test2_element:
    """
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    ns_test1_ns_test2_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="ns_test1 ns_test2",
            min_occurs=1,
            max_occurs=2
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

    value: Optional["str"] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
