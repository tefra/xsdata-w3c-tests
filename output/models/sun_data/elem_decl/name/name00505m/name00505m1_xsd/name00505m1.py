from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Global1:
    class Meta:
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Global2:
    class Meta:
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
