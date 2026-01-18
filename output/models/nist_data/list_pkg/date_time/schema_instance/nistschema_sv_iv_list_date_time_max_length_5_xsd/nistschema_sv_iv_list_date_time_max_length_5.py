from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-maxLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDateTimeMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-dateTime-maxLength-5-NS"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
