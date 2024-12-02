from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-pattern-5-NS"


@dataclass
class NistschemaSvIvListBytePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-pattern-5"
        namespace = "NISTSchema-SV-IV-list-byte-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{3} \-\d{2} \-\d{1} \d{1} \d{2} \d{3} \-\d{3} \-\d{2} \-\d{1}",
            "tokens": True,
        },
    )
