from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-1-NS"

    value: QName = field(
        metadata={
            "required": True,
            "max_length": 1,
        }
    )
