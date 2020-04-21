from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-4-NS"


@dataclass
class NistschemaSvIvUnionShortGYearPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-4"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d{2}"
        )
    )
