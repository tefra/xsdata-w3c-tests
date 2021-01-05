from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    value: str = field(
        init=False,
        default="1.0E-2",
        metadata={
            "required": True,
            "pattern": r"...E..",
        }
    )
