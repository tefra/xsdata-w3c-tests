from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicQnameMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-1-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=1
        )
    )
