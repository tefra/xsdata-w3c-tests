from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Zing:
    class Meta:
        name = "zing"

    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
