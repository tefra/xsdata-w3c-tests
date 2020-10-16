from dataclasses import dataclass, field
from typing import Dict


@dataclass
class T:
    """
    :ivar any_attributes:
    """
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class Eden(T):
    class Meta:
        name = "eden"
