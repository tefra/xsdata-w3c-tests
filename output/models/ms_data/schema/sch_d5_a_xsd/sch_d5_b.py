from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.schema.sch_d5_a_xsd.sch_d5_a import (
    CtA,
)
from output.models.ms_data.schema.sch_d5_a_xsd.sch_d5_c import (
    CtC,
)

__NAMESPACE__ = "ns-a"


@dataclass
class CtB:
    """
    :ivar b1:
    :ivar b2:
    """
    class Meta:
        name = "ct-B"

    b1: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a",
            required=True
        )
    )
    b2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a",
            required=True
        )
    )


@dataclass
class BE1(CtA):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"



@dataclass
class BE3(CtC):
    class Meta:
        name = "b-e3"
        namespace = "ns-a"



@dataclass
class E2(CtB):
    class Meta:
        name = "e2"
        namespace = "ns-a"
