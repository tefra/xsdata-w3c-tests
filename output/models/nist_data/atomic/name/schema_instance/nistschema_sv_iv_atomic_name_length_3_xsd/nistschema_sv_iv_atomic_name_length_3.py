from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-length-3-NS"


@dataclass
class NistschemaSvIvAtomicNameLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-length-3"
        namespace = "NISTSchema-SV-IV-atomic-Name-length-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 60,
        },
    )
