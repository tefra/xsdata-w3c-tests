from dataclasses import dataclass, field
from typing import Any, Dict


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
        default=None,
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
