from dataclasses import dataclass, field

__NAMESPACE__ = "baseTD"


@dataclass
class Test1:
    abc: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class Test(Test1):
    pass


@dataclass
class Root(Test):
    class Meta:
        name = "root"
        namespace = "baseTD"
