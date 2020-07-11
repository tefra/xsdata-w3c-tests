from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Computer:
    """
    :ivar local_apple_com_attributes:
    :ivar local_orange_com_attributes:
    """
    class Meta:
        name = "computer"

    local_apple_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local http://apple.com/",
            required=True
        )
    )
    local_orange_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local http://orange.com/",
            required=True
        )
    )
