from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar list_of_ids_attr:
    :ivar idref_attr:
    """
    class Meta:
        name = "root"

    list_of_ids_attr: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
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
