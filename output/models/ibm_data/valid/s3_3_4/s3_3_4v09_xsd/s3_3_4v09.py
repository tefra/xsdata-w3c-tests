from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class Ids:
    class Meta:
        name = "ids"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class ValueConstraint(Enum):
    ASD = "asd"


@dataclass
class Idrefs:
    class Meta:
        name = "idrefs"

    idref: ValueConstraint = field(
        init=False,
        default=ValueConstraint.ASD,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    a: Optional[Ids] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[Idrefs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
