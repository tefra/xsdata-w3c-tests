from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Ct:
    """
    :ivar value:
    :ivar att:
    """
    class Meta:
        name = "ct"

    value: Optional[str] = field(
        default=None,
    )
    att: Optional[Union[bool, int, str]] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar e:
    """
    class Meta:
        name = "root"

    e: List[Ct] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=3
        )
    )
