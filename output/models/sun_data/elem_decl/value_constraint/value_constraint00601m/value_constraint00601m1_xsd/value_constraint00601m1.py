from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    value: float = field(
        init=False,
        default=0.01,
        metadata={
            "required": True,
        }
    )
