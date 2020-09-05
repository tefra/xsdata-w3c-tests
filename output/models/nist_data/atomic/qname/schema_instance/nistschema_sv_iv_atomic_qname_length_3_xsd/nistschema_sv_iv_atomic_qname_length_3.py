from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-length-3-NS"


@dataclass
class NistschemaSvIvAtomicQnameLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-length-3"
        namespace = "NISTSchema-SV-IV-atomic-QName-length-3-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            length=33
        )
    )
