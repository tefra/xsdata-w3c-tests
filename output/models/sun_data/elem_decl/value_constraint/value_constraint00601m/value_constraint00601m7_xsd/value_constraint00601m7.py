from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    value: str = field(
        default="1.0E-2",
        metadata={
            "pattern": r"...E..",
        }
    )
