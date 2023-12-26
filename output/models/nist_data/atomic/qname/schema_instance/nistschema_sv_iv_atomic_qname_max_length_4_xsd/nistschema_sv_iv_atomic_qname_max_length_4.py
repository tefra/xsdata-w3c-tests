from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicQnameMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-4-NS"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 61,
        },
    )
