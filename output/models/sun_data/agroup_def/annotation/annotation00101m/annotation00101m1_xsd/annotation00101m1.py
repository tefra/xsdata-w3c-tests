from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AGroupDef/annotation"


@dataclass
class A:
    c: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AGroupDef/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
