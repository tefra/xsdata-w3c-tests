from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-pattern-5-NS"


@dataclass
class NistschemaSvIvListPositiveIntegerPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-pattern-5"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\d{1} \d{4} \d{7} \d{10} \d{13} \d{18}",
            tokens=True
        )
    )
