from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-maxLength-2-NS"


@dataclass
class NistschemaSvIvListBase64BinaryMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-base64Binary-maxLength-2-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
            "format": "base64",
        },
    )
