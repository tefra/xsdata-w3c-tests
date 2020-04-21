from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Root:
    """
    :ivar e:
    """
    class Meta:
        name = "root"

    e: List[Union[bool, int, str]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=3
        )
    )
