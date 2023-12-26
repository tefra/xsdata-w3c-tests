from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-length-5-NS"


@dataclass
class NistschemaSvIvAtomicStringLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-length-5"
        namespace = "NISTSchema-SV-IV-atomic-string-length-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 1000,
        },
    )
