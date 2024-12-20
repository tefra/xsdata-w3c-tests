from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-length-2-NS"


@dataclass
class NistschemaSvIvListDateTimeLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-length-2"
        namespace = "NISTSchema-SV-IV-list-dateTime-length-2-NS"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
