from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Root:
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "root"

    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )
