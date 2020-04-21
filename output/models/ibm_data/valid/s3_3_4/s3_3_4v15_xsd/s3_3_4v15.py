from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar value:
    :ivar idref_attr:
    """
    class Meta:
        name = "root"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    idref_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Wrapper:
    """
    :ivar root:
    """
    class Meta:
        name = "wrapper"

    root: Optional[Root] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
