from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Eden:
    class Meta:
        name = "eden"

    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
