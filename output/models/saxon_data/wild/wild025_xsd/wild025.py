from dataclasses import dataclass, field
from typing import Dict


@dataclass
class T:
    adam_com_eve_com_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://adam.com/ http://eve.com/",
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class Eden(T):
    class Meta:
        name = "eden"
