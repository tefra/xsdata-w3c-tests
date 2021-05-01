from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Root:
    class Meta:
        name = "root"

    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        }
    )
