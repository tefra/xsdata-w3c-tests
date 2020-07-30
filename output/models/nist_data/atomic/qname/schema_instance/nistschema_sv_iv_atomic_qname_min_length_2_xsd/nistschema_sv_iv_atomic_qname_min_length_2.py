from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicQnameMinLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-2-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=8
        )
    )
