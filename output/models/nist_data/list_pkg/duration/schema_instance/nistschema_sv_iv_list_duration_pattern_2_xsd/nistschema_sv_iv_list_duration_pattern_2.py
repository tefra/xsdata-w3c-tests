from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-pattern-2-NS"


@dataclass
class NistschemaSvIvListDurationPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-pattern-2"
        namespace = "NISTSchema-SV-IV-list-duration-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"P19\d\dY\d7M\d5DT1\dH\d1M\d8S P20\d\dY0\dM0\dDT\d9H\d9M\d7S P19\d\dY0\dM0\dDT\d0H5\dM0\dS P18\d\dY\d1M\d8DT\d9H1\dM\d5S P19\d\dY0\dM2\dDT\d6H2\dM\d5S P\d\d75Y1\dM0\dDT1\dH\d8M\d5S P17\d\dY\d5M0\dDT\d4H2\dM\d5S P19\d\dY1\dM1\dDT\d8H\d4M3\dS P\d\d93Y0\dM1\dDT1\dH\d9M\d1S P18\d\dY0\dM0\dDT\d4H\d3M\d1S",
            tokens=True
        )
    )
