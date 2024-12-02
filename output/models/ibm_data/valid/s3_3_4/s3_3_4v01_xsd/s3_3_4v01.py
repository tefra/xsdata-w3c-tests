from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AnyAttr:
    class Meta:
        name = "anyAttr"

    id1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    a: Optional[AnyAttr] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
