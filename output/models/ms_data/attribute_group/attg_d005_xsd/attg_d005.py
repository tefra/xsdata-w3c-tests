from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar content:
    :ivar att1:
    :ivar foo:
    :ivar att2:
    :ivar bar:
    :ivar att3:
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
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bar: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_exclusive": 100,
        }
    )
    att3: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
