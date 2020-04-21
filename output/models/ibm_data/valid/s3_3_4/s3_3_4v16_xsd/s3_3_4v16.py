from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar idref_element:
    :ivar list_of_ids_attr:
    """
    class Meta:
        name = "root"

    idref_element: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    list_of_ids_attr: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
