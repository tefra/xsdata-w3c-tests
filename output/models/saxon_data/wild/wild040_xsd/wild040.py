from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Computer:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "computer"

    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any",
            required=True
        )
    )
