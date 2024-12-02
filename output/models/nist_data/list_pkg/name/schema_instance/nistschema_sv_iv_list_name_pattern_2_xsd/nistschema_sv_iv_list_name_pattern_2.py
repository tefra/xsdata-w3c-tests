from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-pattern-2-NS"


@dataclass
class NistschemaSvIvListNamePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-pattern-2"
        namespace = "NISTSchema-SV-IV-list-Name-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\i\c{33} \i\c{52} \i\c{56} \i\c{6} \i\c{22}",
            "tokens": True,
        },
    )
