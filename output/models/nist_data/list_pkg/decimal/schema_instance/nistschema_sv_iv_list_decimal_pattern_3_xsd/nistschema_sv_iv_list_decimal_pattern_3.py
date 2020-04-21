from decimal import Decimal
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-pattern-3-NS"


@dataclass
class NistschemaSvIvListDecimalPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-pattern-3"
        namespace = "NISTSchema-SV-IV-list-decimal-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\-\d{1} \-\d{1}\.\d{2} \.\d{5} \d{1}\.\d{6} \-\d{8}\.\d{1} \-\d{1}\.\d{10} \-\d{11}\.\d{2} \-\d{8}\.\d{10}"
        )
    )
