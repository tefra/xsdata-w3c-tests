from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )
