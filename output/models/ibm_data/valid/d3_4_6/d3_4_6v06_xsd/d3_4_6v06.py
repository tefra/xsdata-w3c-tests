from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    """
    :ivar ele:
    :ivar value:
    :ivar value_1:
    :ivar value_9:
    :ivar value_2:
    :ivar a_a:
    :ivar a_a_a:
    :ivar a_ele:
    """
    ele: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="_ele",
            type="Element",
            namespace="a",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="_-",
            type="Element",
            namespace="a",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    value_1: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="_.",
            type="Element",
            namespace="a",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    value_9: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="_9",
            type="Element",
            namespace="a",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    value_2: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="___",
            type="Element",
            namespace="a",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a_a: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="a",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a_a_a: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="a.a",
            type="Element",
            namespace="a",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a_ele: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ele",
            type="Element",
            namespace="a",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
