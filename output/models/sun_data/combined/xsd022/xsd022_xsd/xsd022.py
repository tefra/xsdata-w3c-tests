from dataclasses import dataclass, field
from typing import List, Optional, Union

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

    child1: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_length=5.0
        )
    )
    child2: List["Root.Child2"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Child2:
        """
        :ivar value:
        """
        value: Optional[Union[bool, str]] = field(
            default=None,
            metadata=dict(
                min_length=5.0
            )
        )
