from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-4-NS"

    value: QName = field(
        metadata={
            "required": True,
            "min_length": 18,
        }
    )
