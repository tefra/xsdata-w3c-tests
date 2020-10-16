from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Zing:
    """
    :ivar any_attributes:
    :ivar local_attributes:
    """
    class Meta:
        name = "zing"

    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
            "required": True,
        }
    )
    local_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
            "required": True,
        }
    )
