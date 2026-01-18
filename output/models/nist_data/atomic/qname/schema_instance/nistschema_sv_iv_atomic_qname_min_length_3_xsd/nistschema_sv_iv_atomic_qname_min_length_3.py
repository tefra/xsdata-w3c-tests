from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-3-NS"

    value: QName = field(
        metadata={
            "required": True,
            "min_length": 50,
        }
    )
