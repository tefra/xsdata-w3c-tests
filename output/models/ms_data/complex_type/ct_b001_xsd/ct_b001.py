from dataclasses import dataclass


@dataclass
class FooType:
    """Annotation information."""
    class Meta:
        name = "fooType"



@dataclass
class Root(FooType):
    class Meta:
        name = "root"
