from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    """
    :ivar foo:
    :ivar other_attributes:
    """
    class Meta:
        name = "attRef"

    foo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
