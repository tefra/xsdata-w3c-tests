from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class Keyname:
    """
    :ivar numid:
    :ivar numname:
    """
    class Meta:
        name = "keyname"

    numid: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Numid",
            type="Element",
            namespace="a",
            required=True
        )
    )
    numname: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Numname",
            type="Element",
            namespace="a",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar number:
    """
    class Meta:
        name = "root"
        namespace = "a"

    number: List[Keyname] = field(
        default_factory=list,
        metadata=dict(
            name="Number",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
