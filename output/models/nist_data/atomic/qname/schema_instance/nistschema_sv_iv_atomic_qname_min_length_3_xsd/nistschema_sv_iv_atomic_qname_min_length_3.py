from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-3-NS"


@dataclass
class NistschemaSvIvAtomicQnameMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-3-NS"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 50,
        },
    )
