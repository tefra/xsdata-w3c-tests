from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Computer:
    class Meta:
        name = "computer"

    w3_org_2001_xmlschema_instance_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
