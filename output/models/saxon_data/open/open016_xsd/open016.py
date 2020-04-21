from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar value:
    :ivar evidence:
    :ivar open_com_element:
    """
    class Meta:
        name = "doc"

    value: Optional[str] = field(
        default=None,
    )
    evidence: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    open_com_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://open.com/",
            min_occurs=1,
            max_occurs=2
        )
    )
