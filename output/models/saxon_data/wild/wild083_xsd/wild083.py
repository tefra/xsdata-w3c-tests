from dataclasses import dataclass, field
from typing import Dict


@dataclass
class B:
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class E1(B):
    class Meta:
        name = "E"

    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class E(E1):
    class Meta:
        name = "e"
