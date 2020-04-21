from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Eden:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "eden"

    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
