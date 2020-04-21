from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Zz:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "zz"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ZzDouble(Zz):
    class Meta:
        name = "zz-double"


@dataclass
class ZzInteger(Zz):
    class Meta:
        name = "zz-integer"


@dataclass
class Zing:
    """
    :ivar a:
    """
    class Meta:
        name = "zing"

    a: List[Union[Zz, ZzDouble, ZzInteger]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
