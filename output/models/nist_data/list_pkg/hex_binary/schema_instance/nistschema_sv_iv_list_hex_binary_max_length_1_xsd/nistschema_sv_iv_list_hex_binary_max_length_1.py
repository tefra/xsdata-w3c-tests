from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-maxLength-1-NS"


@dataclass
class NistschemaSvIvListHexBinaryMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-hexBinary-maxLength-1-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
            "format": "base16",
        },
    )
