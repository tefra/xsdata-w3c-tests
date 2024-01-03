from dataclasses import dataclass, field
from typing import List, Optional, Any


@dataclass
class Computer:
    class Meta:
        name = "computer"

    cpu: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPU",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    memory: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    monitor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    speaker: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class QuietComputer(Computer):
    class Meta:
        name = "quietComputer"

    speaker: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
