from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-maxLength-3-NS"


@dataclass
class NistschemaSvIvListDateTimeMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-dateTime-maxLength-3-NS"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        },
    )
