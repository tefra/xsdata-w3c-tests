from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List

__NAMESPACE__ = "http://schemas.microsoft.com/2003/10/Serialization/"


@dataclass
class Array:
    """
    :ivar item:
    :ivar item_type:
    :ivar dimensions:
    :ivar lower_bounds:
    """
    class Meta:
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    item: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="Item",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            nillable=True
        )
    )
    item_type: QName = field(
        default=QName("http://www.w3.org/2001/XMLSchema", "anyType"),
        metadata=dict(
            name="ItemType",
            type="Attribute",
            namespace="http://schemas.microsoft.com/2003/10/Serialization/",
            required=True
        )
    )
    dimensions: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="Dimensions",
            type="Attribute",
            required=True,
            tokens=True
        )
    )
    lower_bounds: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="LowerBounds",
            type="Attribute",
            required=True,
            tokens=True
        )
    )
