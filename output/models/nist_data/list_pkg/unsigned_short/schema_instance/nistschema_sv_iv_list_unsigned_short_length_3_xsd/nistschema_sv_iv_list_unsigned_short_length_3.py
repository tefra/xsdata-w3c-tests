from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-length-3-NS"


@dataclass
class NistschemaSvIvListUnsignedShortLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-length-3"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-length-3-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
