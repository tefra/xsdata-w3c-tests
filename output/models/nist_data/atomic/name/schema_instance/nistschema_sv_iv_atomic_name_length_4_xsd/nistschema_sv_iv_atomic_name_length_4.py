from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-length-4-NS"


@dataclass
class NistschemaSvIvAtomicNameLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-length-4"
        namespace = "NISTSchema-SV-IV-atomic-Name-length-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 6,
        },
    )
