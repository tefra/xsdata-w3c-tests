from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-pattern-4-NS"


@dataclass
class NistschemaSvIvListDurationPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-pattern-4"
        namespace = "NISTSchema-SV-IV-list-duration-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"P\d\d34Y0\dM\d7DT1\dH3\dM\d3S P18\d\dY0\dM1\dDT\d2H1\dM0\dS P18\d\dY1\dM\d3DT\d6H\d7M4\dS P17\d\dY1\dM\d0DT\d8H\d5M\d0S P\d\d55Y0\dM\d5DT1\dH\d4M1\dS P\d\d22Y\d3M1\dDT1\dH1\dM\d3S P\d\d14Y1\dM\d9DT\d8H5\dM1\dS P\d\d44Y0\dM\d3DT0\dH\d1M\d1S",
            "tokens": True,
        }
    )
