from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    """
    :ivar other_attributes:
    """
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )
