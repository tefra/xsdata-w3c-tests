from decimal import Decimal
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-pattern-2-NS"


@dataclass
class NistschemaSvIvListDecimalPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-pattern-2"
        namespace = "NISTSchema-SV-IV-list-decimal-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\d{1} \-\.\d{3} \d{4}\.\d{1} \d{6}\.\d{1} \d{7}\.\d{2} \-\d{5}\.\d{6} \d{13} \d{4}\.\d{14}"
        )
    )