from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-length-1-NS"


@dataclass
class NistschemaSvIvAtomicQnameLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-length-1"
        namespace = "NISTSchema-SV-IV-atomic-QName-length-1-NS"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
            "length": 1,
        }
    )
