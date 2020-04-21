from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class Root:
    """
    :ivar list_of_ids_element:
    :ivar idref_element:
    """
    class Meta:
        name = "root"
        namespace = "a"

    list_of_ids_element: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    idref_element: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
