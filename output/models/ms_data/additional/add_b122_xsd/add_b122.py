from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Att1:
    """
    :ivar att:
    """
    class Meta:
        name = "att1"

    att: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Att2:
    """
    :ivar att1:
    :ivar att2:
    """
    class Meta:
        name = "att2"

    att1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class E1:
    """
    :ivar value:
    """
    class Meta:
        name = "e1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            length=4
        )
    )


@dataclass
class M3:
    """
    :ivar e31:
    :ivar att:
    """
    class Meta:
        name = "m3"

    e31: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2
        )
    )
    att: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class M6:
    """
    :ivar any_element:
    """
    class Meta:
        name = "m6"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class E2(Att1):
    class Meta:
        name = "e2"


@dataclass
class E3(M3):
    class Meta:
        name = "e3"


@dataclass
class E6(M6):
    class Meta:
        name = "e6"


@dataclass
class E7(Att1):
    class Meta:
        name = "e7"


@dataclass
class E8(Att1):
    class Meta:
        name = "e8"


@dataclass
class M4:
    """
    :ivar e41:
    :ivar e3:
    :ivar att:
    """
    class Meta:
        name = "m4"

    e41: List[Att2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=3,
            sequential=True
        )
    )
    e3: List[E3] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=3,
            sequential=True
        )
    )
    att: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class E4(M4):
    class Meta:
        name = "e4"


@dataclass
class M5:
    """
    :ivar e3:
    :ivar e4:
    :ivar e5:
    :ivar att:
    """
    class Meta:
        name = "m5"

    e3: List[E3] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e4: List[E4] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e5: List["E5"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    att: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class E5(M5):
    class Meta:
        name = "e5"


@dataclass
class Ct1:
    """
    :ivar e1:
    :ivar e2:
    :ivar e3:
    :ivar e4:
    :ivar e5:
    :ivar e6:
    :ivar e7:
    :ivar e8:
    """
    class Meta:
        name = "ct1"

    e1: Optional[E1] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    e2: Optional[E2] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    e3: List[E3] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e4: List[E4] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e5: List[E5] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e6: List[E6] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e7: List[E7] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e8: List[E8] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(Ct1):
    class Meta:
        name = "root"
