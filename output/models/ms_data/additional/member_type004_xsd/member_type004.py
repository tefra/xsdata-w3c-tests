from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Ct:
    """
    :ivar value:
    :ivar att1:
    :ivar att2:
    :ivar att3:
    """
    class Meta:
        name = "ct"

    value: Optional[str] = field(
        default=None,
    )
    att1: Union[bool, int, str] = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Union[bool, int, str] = field(
        default=5,
        metadata={
            "type": "Attribute",
        }
    )
    att3: Union[bool, int, str] = field(
        default="abc",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    """
    :ivar e:
    """
    class Meta:
        name = "root"

    e: List[Ct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
