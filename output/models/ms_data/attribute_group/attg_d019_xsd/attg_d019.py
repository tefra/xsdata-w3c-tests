from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class AttgRef:
    """
    :ivar att1:
    :ivar any_attributes: testing
    """
    class Meta:
        name = "attgRef"

    att1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    any_attributes: Dict = field(
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

    elem: List[AttgRef] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=10
        )
    )
