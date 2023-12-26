from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Global:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"false",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    value: str = field(
        default="",
        metadata={
            "pattern": r"false",
        },
    )
