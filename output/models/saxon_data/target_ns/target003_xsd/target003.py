from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class B:
    target003_com_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.target003.com/",
        }
    )


@dataclass
class R(B):
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.target003.com/",
        }
    )


@dataclass
class Parent(R):
    class Meta:
        name = "parent"
