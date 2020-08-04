from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    """
    :ivar ns_test1_ns_test2_attributes:
    """
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    ns_test1_ns_test2_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="ns_test1 ns_test2"
        )
    )
