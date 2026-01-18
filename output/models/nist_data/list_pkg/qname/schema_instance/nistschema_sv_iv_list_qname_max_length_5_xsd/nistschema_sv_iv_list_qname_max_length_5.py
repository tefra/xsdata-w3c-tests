from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-maxLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListQnameMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-QName-maxLength-5-NS"

    value: list[QName] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
