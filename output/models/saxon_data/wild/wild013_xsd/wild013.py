from dataclasses import dataclass, field
from typing import Dict


@dataclass
class B:
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class E(B):
    pass


@dataclass
class Eden(E):
    class Meta:
        name = "eden"
