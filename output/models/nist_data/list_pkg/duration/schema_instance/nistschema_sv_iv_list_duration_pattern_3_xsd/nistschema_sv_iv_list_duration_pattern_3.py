from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-pattern-3-NS"


@dataclass
class NistschemaSvIvListDurationPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-pattern-3"
        namespace = "NISTSchema-SV-IV-list-duration-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"P18\d\dY1\dM\d0DT0\dH\d1M3\dS P\d\d87Y0\dM0\dDT\d3H4\dM\d7S P\d\d19Y0\dM\d6DT\d6H3\dM1\dS P19\d\dY\d5M0\dDT\d0H\d5M\d5S P19\d\dY1\dM\d3DT\d4H5\dM3\dS P\d\d22Y0\dM\d9DT1\dH2\dM\d1S P\d\d66Y\d2M\d1DT1\dH3\dM2\dS P\d\d20Y\d6M0\dDT\d5H1\dM\d7S P17\d\dY\d1M\d4DT1\dH\d3M\d4S P19\d\dY0\dM1\dDT0\dH4\dM4\dS"
        )
    )
