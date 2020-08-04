from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar list_of_ids:
    :ivar idref:
    """
    class Meta:
        name = "root"

    list_of_ids: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            tokens=True
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
