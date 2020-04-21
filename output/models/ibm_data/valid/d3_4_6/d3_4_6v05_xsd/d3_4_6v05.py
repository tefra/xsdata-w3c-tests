from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    """
    :ivar x2_vs_zq:
    :ivar xy0:
    :ivar xy4:
    :ivar xzk:
    :ivar x19f:
    :ivar yv9h:
    :ivar ys5h:
    :ivar zwxl:
    """
    x2_vs_zq: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="_ele",
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    xy0: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="_-",
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    xy4: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="_.",
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    xzk: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="_9",
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    x19f: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="___",
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    yv9h: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="a_a",
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    ys5h: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="a.a",
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    zwxl: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ele",
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
