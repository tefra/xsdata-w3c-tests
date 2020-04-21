from dataclasses import dataclass


@dataclass
class FooType:
    class Meta:
        name = "fooType"



@dataclass
class Root(FooType):
    class Meta:
        name = "root"
