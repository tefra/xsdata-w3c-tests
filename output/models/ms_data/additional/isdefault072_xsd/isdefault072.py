from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://schemas.microsoft.com/2003/10/Serialization/"


@dataclass
class Array:
    class Meta:
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    item: List[object] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    item_type: QName = field(
        default=QName("{http://www.w3.org/2001/XMLSchema}anyType"),
        metadata={
            "name": "ItemType",
            "type": "Attribute",
            "namespace": "http://schemas.microsoft.com/2003/10/Serialization/",
        }
    )
    dimensions: List[int] = field(
        default_factory=lambda: [
            1,
        ],
        metadata={
            "name": "Dimensions",
            "type": "Attribute",
            "tokens": True,
        }
    )
    lower_bounds: List[int] = field(
        default_factory=lambda: [
            0,
        ],
        metadata={
            "name": "LowerBounds",
            "type": "Attribute",
            "tokens": True,
        }
    )
