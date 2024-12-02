from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-length-5-NS"


@dataclass
class NistschemaSvIvListBase64BinaryLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-length-5"
        namespace = "NISTSchema-SV-IV-list-base64Binary-length-5-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
            "format": "base64",
        },
    )
