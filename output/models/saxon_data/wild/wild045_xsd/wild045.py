from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class ExtendedComputer:
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "extendedComputer"

    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )


@dataclass
class Computer(ExtendedComputer):
    class Meta:
        name = "computer"
