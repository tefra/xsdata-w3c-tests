from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-4-NS"


@dataclass
class NistschemaSvIvAtomicQnameMinLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-4-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=18.0
        )
    )
