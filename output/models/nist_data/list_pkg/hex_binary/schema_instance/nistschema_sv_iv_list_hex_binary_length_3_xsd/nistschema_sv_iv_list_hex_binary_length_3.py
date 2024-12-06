from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-length-3-NS"


@dataclass
class NistschemaSvIvListHexBinaryLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-length-3"
        namespace = "NISTSchema-SV-IV-list-hexBinary-length-3-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
            "format": "base16",
        },
    )
