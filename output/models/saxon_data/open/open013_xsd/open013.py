from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar open_com_element:
    """
    class Meta:
        name = "doc"

    open_com_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://open.com/",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
