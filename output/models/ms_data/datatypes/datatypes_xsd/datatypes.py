from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Data:
    """
    :ivar any_element:
    """
    class Meta:
        name = "data"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Item:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "item"

    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
