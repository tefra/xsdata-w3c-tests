from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            tokens=True
        )
    )
