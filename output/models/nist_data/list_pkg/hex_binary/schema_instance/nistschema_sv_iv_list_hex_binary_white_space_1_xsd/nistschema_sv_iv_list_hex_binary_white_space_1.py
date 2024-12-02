from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListHexBinaryWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-hexBinary-whiteSpace-1-NS"

    value: list[bytes] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
            "format": "base16",
        },
    )
