from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Root:
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "root"

    local_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )
