from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"

    value: Optional[object] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"

    value: Optional[object] = field(
        default=None,
        metadata=dict(
            required=True
        )
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
class C(Ct4):
    class Meta:
        name = "c"


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
    b: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    a: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    item: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
