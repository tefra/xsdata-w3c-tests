from dataclasses import dataclass, field
from typing import Dict


@dataclass
class ExtendedComputer:
    class Meta:
        name = "extendedComputer"

    local_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        }
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class Computer(ExtendedComputer):
    class Meta:
        name = "computer"
