from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicNamePattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-Name-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\i\c{14}"
        )
    )
