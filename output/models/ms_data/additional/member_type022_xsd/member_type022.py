from dataclasses import dataclass, field
from typing import List, Union

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar e:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    e: List[Union[bool, int, str]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=3
        )
    )