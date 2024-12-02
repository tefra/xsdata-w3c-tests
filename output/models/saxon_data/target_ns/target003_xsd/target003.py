from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class B:
    target003_com_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.target003.com/",
        },
    )


@dataclass
class R(B):
    target003_com_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.target003.com/",
        },
    )


@dataclass
class Parent(R):
    class Meta:
        name = "parent"
