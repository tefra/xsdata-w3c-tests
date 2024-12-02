from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-maxLength-1-NS"


@dataclass
class NistschemaSvIvListDateTimeMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-dateTime-maxLength-1-NS"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
