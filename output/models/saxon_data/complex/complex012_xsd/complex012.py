from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar content:
    :ivar e:
    """
    class Meta:
        name = "root"
        nillable = True

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
    e: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
