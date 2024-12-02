from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-length-3-NS"


@dataclass
class NistschemaSvIvListBase64BinaryLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-length-3"
        namespace = "NISTSchema-SV-IV-list-base64Binary-length-3-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
            "format": "base64",
        },
    )
