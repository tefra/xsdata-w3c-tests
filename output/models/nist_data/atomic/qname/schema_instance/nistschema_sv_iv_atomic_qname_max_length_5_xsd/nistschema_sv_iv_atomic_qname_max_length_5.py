from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-5-NS"


@dataclass
class NistschemaSvIvAtomicQnameMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-5"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-5-NS"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
