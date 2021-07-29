from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"false",
        }
    )
