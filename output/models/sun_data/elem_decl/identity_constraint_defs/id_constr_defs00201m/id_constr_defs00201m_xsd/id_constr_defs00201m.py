from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    account: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Account",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    manager: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Manager",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
