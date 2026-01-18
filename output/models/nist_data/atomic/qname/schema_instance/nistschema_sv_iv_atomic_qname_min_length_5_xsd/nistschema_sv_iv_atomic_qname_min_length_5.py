from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-5-NS"

    value: QName = field(
        metadata={
            "required": True,
            "min_length": 64,
        }
    )
