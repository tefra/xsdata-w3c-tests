from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-pattern-5-NS"


@dataclass
class NistschemaSvIvListDurationPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-pattern-5"
        namespace = "NISTSchema-SV-IV-list-duration-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"P17\d\dY\d4M\d9DT\d4H\d0M\d8S P\d\d77Y\d0M\d1DT\d8H2\dM\d4S P17\d\dY0\dM1\dDT\d1H5\dM\d6S P\d\d90Y0\dM\d6DT\d1H5\dM5\dS P19\d\dY\d8M2\dDT\d4H\d6M1\dS P20\d\dY0\dM0\dDT1\dH\d5M\d3S",
            tokens=True
        )
    )
