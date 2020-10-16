from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Doc:
    """
    :ivar content:
    :ivar att1:
    :ivar foo:
    :ivar other_attributes:
    """
    class Meta:
        name = "doc"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    foo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
