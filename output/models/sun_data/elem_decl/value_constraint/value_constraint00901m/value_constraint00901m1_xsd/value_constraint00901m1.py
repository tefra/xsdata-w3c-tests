from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    value: object = field(
        init=False,
        default="alpha beta",
        metadata={
            "required": True,
        }
    )
