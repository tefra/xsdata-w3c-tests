from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-pattern-1-NS"


@dataclass
class NistschemaSvIvListHexBinaryPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-pattern-1"
        namespace = "NISTSchema-SV-IV-list-hexBinary-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[0-9A-F]{22} [0-9A-F]{70} [0-9A-F]{66} [0-9A-F]{2} [0-9A-F]{30} [0-9A-F]{38}",
            "tokens": True,
        },
    )
