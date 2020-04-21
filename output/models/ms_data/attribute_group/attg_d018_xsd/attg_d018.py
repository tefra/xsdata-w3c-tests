from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class AttgRef:
    """
    :ivar att1:
    :ivar any_attributes:
    """
    class Meta:
        name = "attgRef"

    att1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[AttgRef] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
