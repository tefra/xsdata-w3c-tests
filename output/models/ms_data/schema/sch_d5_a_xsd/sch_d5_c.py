from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.schema.sch_d5_a_xsd.sch_d5_a import (
    CtA,
)
from output.models.ms_data.schema.sch_d5_a_xsd.sch_d5_b import (
    CtB,
)

__NAMESPACE__ = "ns-a"


@dataclass
class CtC:
    """
    :ivar c1:
    :ivar c2:
    """
    class Meta:
        name = "ct-C"

    c1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    c2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class CE1(CtA):
    class Meta:
        name = "c-e1"
        namespace = "ns-a"


@dataclass
class CE2(CtB):
    class Meta:
        name = "c-e2"
        namespace = "ns-a"


@dataclass
class E3(CtC):
    class Meta:
        name = "e3"
        namespace = "ns-a"