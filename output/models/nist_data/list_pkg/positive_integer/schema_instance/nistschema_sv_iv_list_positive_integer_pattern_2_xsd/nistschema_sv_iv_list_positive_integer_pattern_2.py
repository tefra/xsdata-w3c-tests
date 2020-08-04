from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-pattern-2-NS"


@dataclass
class NistschemaSvIvListPositiveIntegerPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-pattern-2"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\d{1} \d{3} \d{5} \d{7} \d{9} \d{11} \d{18}",
            tokens=True
        )
    )
