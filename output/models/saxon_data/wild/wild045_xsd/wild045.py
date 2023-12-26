from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Computer1:
    class Meta:
        name = "computer"

    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass
class ExtendedComputer(Computer1):
    class Meta:
        name = "extendedComputer"


@dataclass
class Computer(ExtendedComputer):
    class Meta:
        name = "computer"
