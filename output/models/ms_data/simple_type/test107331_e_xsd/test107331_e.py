from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Ct1:
    """
    :ivar value:
    """
    class Meta:
        name = "ct1"

    value: Optional[object] = field(
        default=None,
    )


@dataclass
class Ct3:
    """
    :ivar elem:
    """
    class Meta:
        name = "ct3"

    elem: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Ct4:
    """
    :ivar value:
    :ivar name:
    :ivar type:
    :ivar state:
    """
    class Meta:
        name = "ct4"

    value: Optional[str] = field(
        default=None,
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    type: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    state: Optional["Ct4.State"] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )

    class State(Enum):
        """
        :cvar VALUE_0:
        :cvar VALUE_1:
        :cvar VALUE_2:
        """
        VALUE_0 = 0
        VALUE_1 = 1
        VALUE_2 = 2


@dataclass
class Item:
    """
    :ivar value:
    """
    class Meta:
        name = "item"

    value: Optional[object] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class A(Ct1):
    class Meta:
        name = "a"


@dataclass
class C(Ct4):
    class Meta:
        name = "c"


@dataclass
class Ct2(Ct1):
    class Meta:
        name = "ct2"


@dataclass
class B(Ct2):
    class Meta:
        name = "b"


@dataclass
class Root:
    """
    :ivar c:
    :ivar b:
    :ivar a:
    :ivar item:
    """
    class Meta:
        name = "root"

    c: List[C] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    b: List[B] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    a: List[A] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    item: List[Item] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
