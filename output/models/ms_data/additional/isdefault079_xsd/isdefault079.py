from dataclasses import dataclass, field


@dataclass
class RegistryValueModOpSetType:
    regvalueop: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )


@dataclass
class Regvaluemodopset(RegistryValueModOpSetType):
    class Meta:
        name = "regvaluemodopset"
