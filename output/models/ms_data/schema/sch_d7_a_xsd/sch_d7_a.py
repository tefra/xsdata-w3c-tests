from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.schema.sch_d7_a_xsd.sch_d7_c import (
    CtC,
)

__NAMESPACE__ = "ns-a"


@dataclass
class CtA:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "ct-A"

    a1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a",
            required=True
        )
    )
    a2: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ns-a"

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
class AE3(CtC):
    class Meta:
        name = "a-e3"
        namespace = "ns-a"



@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-a"
