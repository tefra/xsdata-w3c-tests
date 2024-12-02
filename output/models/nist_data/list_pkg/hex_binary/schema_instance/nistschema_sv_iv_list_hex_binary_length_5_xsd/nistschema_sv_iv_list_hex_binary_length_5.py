from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-length-5-NS"


@dataclass
class NistschemaSvIvListHexBinaryLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-length-5"
        namespace = "NISTSchema-SV-IV-list-hexBinary-length-5-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
            "format": "base16",
        },
    )
