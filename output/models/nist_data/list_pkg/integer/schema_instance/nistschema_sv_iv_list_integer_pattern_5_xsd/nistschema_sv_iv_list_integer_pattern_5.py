from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-integer-pattern-5-NS"


@dataclass
class NistschemaSvIvListIntegerPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-integer-pattern-5"
        namespace = "NISTSchema-SV-IV-list-integer-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\-\d{18} \-\d{9} \-\d{5} \-\d{1} \d{3} \d{7} \d{18}",
            tokens=True
        )
    )
