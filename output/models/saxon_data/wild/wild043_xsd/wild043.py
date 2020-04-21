from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Computer:
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "computer"

    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local",
            required=True
        )
    )
