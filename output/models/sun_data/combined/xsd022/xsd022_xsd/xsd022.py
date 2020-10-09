from dataclasses import dataclass, field
from typing import List, Union

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    """
    :ivar child1:
    :ivar child2:
    """
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    child1: List[List[str]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_length=5,
            tokens=True
        )
    )
    child2: List[Union[bool, str]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_length=5
        )
    )
