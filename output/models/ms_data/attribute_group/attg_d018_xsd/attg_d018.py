from dataclasses import dataclass, field
from typing import Dict, Optional


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
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
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
