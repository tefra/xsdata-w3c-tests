from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-negativeInteger-pattern-5-NS"


@dataclass
class NistschemaSvIvListNegativeIntegerPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-negativeInteger-pattern-5"
        namespace = "NISTSchema-SV-IV-list-negativeInteger-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\-\d{1} \-\d{3} \-\d{5} \-\d{7} \-\d{9} \-\d{11} \-\d{13} \-\d{18}",
            "tokens": True,
        }
    )
