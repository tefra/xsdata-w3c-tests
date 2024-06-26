from dataclasses import dataclass, field
from typing import Dict


@dataclass
class B:
    abel_com_adam_com_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://abel.com/ http://adam.com/",
        },
    )


@dataclass
class E(B):
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class Eden(E):
    class Meta:
        name = "eden"
