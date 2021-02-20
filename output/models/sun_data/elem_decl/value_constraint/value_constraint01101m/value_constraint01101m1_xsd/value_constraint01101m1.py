from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    element: float = field(
        init=False,
        default=0.0,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
            "max_inclusive": 0.0,
        }
    )
