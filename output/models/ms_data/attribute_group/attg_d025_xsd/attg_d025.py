from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    foo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
