from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttgRef:
    class Meta:
        name = "attgRef"

    att1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[AttgRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
