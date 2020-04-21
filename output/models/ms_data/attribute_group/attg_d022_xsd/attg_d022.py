from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class Doc:
    """
    :ivar att1:
    :ivar foo:
    :ivar other_attributes:
    """
    class Meta:
        name = "doc"

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
