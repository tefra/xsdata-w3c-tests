from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ids:
    """
    :ivar id:
    """
    class Meta:
        name = "ids"

    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


class ValueConstraint(Enum):
    """
    :cvar ASD:
    """
    ASD = "asd"


@dataclass
class Idrefs:
    """
    :ivar idref:
    """
    class Meta:
        name = "idrefs"

    idref: ValueConstraint = field(
        init=False,
        default="asd",
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "root"

    a: Optional[Ids] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[Idrefs] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
