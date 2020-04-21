from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v04"


@dataclass
class Root:
    """
    :ivar ely_mdmin_inclusive_min_inclusive:
    :ivar ely_mdmin_inclusive_min_exclusive:
    :ivar ely_mdmin_inclusive_max_inclusive:
    :ivar ely_mdmin_inclusive_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v04"

    ely_mdmin_inclusive_min_inclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDMinInclusive_MinInclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_inclusive="P1DT535.4S"
        )
    )
    ely_mdmin_inclusive_min_exclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDMinInclusive_MinExclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_exclusive="P2D",
            min_inclusive="P1D"
        )
    )
    ely_mdmin_inclusive_max_inclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDMinInclusive_MaxInclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_inclusive="P1D",
            max_inclusive="P3452DT2H"
        )
    )
    ely_mdmin_inclusive_max_exclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDMinInclusive_MaxExclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_inclusive="P1D",
            max_exclusive="P43DT43M"
        )
    )
