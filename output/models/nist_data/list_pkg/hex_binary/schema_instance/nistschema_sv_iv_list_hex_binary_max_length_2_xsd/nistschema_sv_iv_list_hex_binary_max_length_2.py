from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-maxLength-2-NS"


@dataclass
class NistschemaSvIvListHexBinaryMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-hexBinary-maxLength-2-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
            "format": "base16",
        },
    )
