from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-length-4-NS"


@dataclass
class NistschemaSvIvAtomicQnameLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-length-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-length-4-NS"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
            "length": 34,
        }
    )
