from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "tns"


@dataclass
class ChildType:
    """
    :ivar content:
    :ivar type1:
    :ivar type2:
    """
    class Meta:
        name = "childType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type1: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    """
    :ivar child:
    """
    class Meta:
        name = "root"
        namespace = "tns"

    child: List[Union[ChildType, bool, int]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
