from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=4,
            sequential=True
        )
    )
    a2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=4,
            sequential=True
        )
    )
