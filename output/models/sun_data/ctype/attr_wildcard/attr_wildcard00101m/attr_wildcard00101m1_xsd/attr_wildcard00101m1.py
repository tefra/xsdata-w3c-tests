from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "attrWildcard"


@dataclass
class A1:
    class Meta:
        name = "A"

    b: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
class A(A1):
    class Meta:
        name = "a"
        namespace = "attrWildcard"
