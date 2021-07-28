from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicQnameWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-QName-whiteSpace-1-NS"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
