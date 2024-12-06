from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListBooleanWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-boolean-whiteSpace-1-NS"

    value: list[bool] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
