from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-pattern-4-NS"


@dataclass
class NistschemaSvIvUnionAnyUriFloatPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-pattern-4"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\c{3,6}://(\c{1,5}\.){1,4}\c{3}",
        },
    )
