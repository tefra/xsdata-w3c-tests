from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t_or_u: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "t",
                    "type": str,
                },
                {
                    "name": "u",
                    "type": Decimal,
                },
            ),
        }
    )


@dataclass
class T:
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class U:
    class Meta:
        name = "u"
        namespace = "myNS.tempuri.org"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
