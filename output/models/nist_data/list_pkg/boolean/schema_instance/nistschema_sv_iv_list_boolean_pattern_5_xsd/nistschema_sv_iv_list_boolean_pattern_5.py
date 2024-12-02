from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-5-NS"


@dataclass
class NistschemaSvIvListBooleanPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-5"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[1]{1} [1]{1} false [1]{1} false [1]{1} false false [0]{1} [1]{1}",
            "tokens": True,
        },
    )
