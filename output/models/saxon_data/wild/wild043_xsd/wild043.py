from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Computer:
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "computer"

    local_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local",
            required=True
        )
    )
