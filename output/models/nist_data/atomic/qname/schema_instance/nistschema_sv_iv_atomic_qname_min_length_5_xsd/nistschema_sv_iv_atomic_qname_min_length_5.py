from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-5-NS"


@dataclass
class NistschemaSvIvAtomicQnameMinLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-5-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=64
        )
    )
