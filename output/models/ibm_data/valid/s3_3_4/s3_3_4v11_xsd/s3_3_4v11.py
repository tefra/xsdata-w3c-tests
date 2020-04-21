from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Root:
    """
    :ivar union_of_ids:
    :ivar idref:
    """
    class Meta:
        name = "root"

    union_of_ids: List[Union[int, str]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    idref: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
