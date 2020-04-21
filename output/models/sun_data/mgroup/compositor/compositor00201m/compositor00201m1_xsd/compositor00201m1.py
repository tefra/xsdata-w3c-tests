from dataclasses import dataclass

__NAMESPACE__ = "compositor"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "compositor"
