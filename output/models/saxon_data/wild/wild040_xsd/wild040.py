from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Computer:
    class Meta:
        name = "computer"

    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
