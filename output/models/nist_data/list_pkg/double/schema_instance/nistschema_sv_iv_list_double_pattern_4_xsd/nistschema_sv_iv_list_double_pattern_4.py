from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-pattern-4-NS"


@dataclass
class NistschemaSvIvListDoublePattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-double-pattern-4"
        namespace = "NISTSchema-SV-IV-list-double-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\d{1}E\-\d{3} \d{1}\.\d{2}E\-\d{2} \d{1}\.\d{4}E\-\d{1} \d{1}\.\d{6}E\d{1} \d{1}\.\d{8}E\d{2} \d{1}\.\d{10}E\d{3} \d{1}\.\d{16}E\-\d{3}",
            tokens=True
        )
    )
