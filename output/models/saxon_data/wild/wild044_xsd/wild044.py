from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Computer:
    """
    :ivar apple_com_attributes:
    :ivar orange_com_attributes:
    """
    class Meta:
        name = "computer"

    apple_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local http://apple.com/",
            required=True
        )
    )
    orange_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local http://orange.com/",
            required=True
        )
    )
