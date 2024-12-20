from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-minLength-5-NS"


@dataclass
class NistschemaSvIvListHexBinaryMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-minLength-5"
        namespace = "NISTSchema-SV-IV-list-hexBinary-minLength-5-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
            "format": "base16",
        },
    )
