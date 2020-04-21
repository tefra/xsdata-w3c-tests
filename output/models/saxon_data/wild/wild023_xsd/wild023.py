from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class T:
    """
    :ivar any_attributes:
    """
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class Eden(T):
    class Meta:
        name = "eden"
