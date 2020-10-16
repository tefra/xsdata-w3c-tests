from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar key:
    :ivar ref:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    key: List[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ref: List[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
