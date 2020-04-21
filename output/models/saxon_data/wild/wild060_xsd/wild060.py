from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class ExtendedZing:
    """
    :ivar any_attributes:
    :ivar local_attributes:
    """
    class Meta:
        name = "extendedZing"

    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )


@dataclass
class Zing(ExtendedZing):
    class Meta:
        name = "zing"
