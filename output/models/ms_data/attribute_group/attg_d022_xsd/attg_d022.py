from dataclasses import dataclass, field
from lxml.etree import QName
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
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    foo: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    other_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )
