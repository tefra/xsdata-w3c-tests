from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Root:
    """
    :ivar idref_element:
    :ivar union_of_ids_attr1:
    :ivar union_of_ids_attr2:
    :ivar union_of_ids_attr3:
    """
    class Meta:
        name = "root"

    idref_element: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    union_of_ids_attr1: Optional[Union[int, bool, str]] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    union_of_ids_attr2: Optional[Union[int, bool, str]] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    union_of_ids_attr3: Optional[Union[int, bool, str]] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
