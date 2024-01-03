from dataclasses import dataclass, field
from typing import Dict, Any


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
class R(B):
    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    eve_com_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://eve.com/",
        },
    )


@dataclass
class Eden(R):
    class Meta:
        name = "eden"
