from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-minLength-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-QName-minLength-2-NS"

    value: QName = field(
        metadata={
            "min_length": 8,
        }
    )
