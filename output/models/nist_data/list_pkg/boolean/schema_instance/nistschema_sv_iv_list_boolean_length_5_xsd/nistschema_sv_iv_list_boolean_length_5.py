from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-length-5-NS"


@dataclass
class NistschemaSvIvListBooleanLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-length-5"
        namespace = "NISTSchema-SV-IV-list-boolean-length-5-NS"

    value: list[bool] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
