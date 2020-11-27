from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Computer:
    class Meta:
        name = "computer"

    local_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
            "required": True,
        }
    )
