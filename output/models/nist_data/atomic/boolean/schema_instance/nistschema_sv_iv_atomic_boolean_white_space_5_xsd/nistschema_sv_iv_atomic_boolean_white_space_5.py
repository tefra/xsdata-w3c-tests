from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5-NS"


@dataclass
class NistschemaSvIvAtomicBooleanWhiteSpace5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5-NS"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True,
            white_space="collapse"
        )
    )
