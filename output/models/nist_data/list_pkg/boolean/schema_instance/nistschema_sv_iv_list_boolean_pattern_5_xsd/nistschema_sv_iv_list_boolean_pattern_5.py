from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-5-NS"


@dataclass
class NistschemaSvIvListBooleanPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-5"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"[1]{1} [1]{1} false [1]{1} false [1]{1} false false [0]{1} [1]{1}",
            tokens=True
        )
    )
