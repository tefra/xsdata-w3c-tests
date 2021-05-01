from dataclasses import dataclass, field
from typing import Dict


@dataclass
class T:
    any_attributes: Dict[str, str] = field(
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
