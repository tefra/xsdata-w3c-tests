from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Zing:
    """
    :ivar any_attributes:
    :ivar local_attributes:
    """
    class Meta:
        name = "zing"

    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any",
            required=True
        )
    )
    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local",
            required=True
        )
    )