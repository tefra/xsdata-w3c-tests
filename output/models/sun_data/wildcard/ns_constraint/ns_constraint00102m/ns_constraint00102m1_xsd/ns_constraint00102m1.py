from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
