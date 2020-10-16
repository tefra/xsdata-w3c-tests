from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Computer:
    """
    :ivar w3_org_2001_xmlschema_instance_attributes:
    """
    class Meta:
        name = "computer"

    w3_org_2001_xmlschema_instance_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        }
    )
