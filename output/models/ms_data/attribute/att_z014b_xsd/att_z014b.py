from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Base:
    class Meta:
        name = "base"

    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: Optional[str] = field(
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
class Doc(Base):
    class Meta:
        name = "doc"
