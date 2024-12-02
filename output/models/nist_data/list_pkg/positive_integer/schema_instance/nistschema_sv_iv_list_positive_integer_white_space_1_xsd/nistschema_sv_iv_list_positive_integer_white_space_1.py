from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListPositiveIntegerWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-whiteSpace-1-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
