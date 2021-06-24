from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Element:
    class Meta:
        namespace = "ElemDecl/valueConstraint"

    value: str = field(
        init=False,
        default="1.0e-2",
        metadata={
            "pattern": r"...[Ee]..",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    element: str = field(
        init=False,
        default="1.0e-2",
        metadata={
            "name": "Element",
            "type": "Element",
            "pattern": r"...[Ee]..",
        }
    )
