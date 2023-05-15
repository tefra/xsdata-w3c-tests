from output.models.sun_data.combined.xsd022.xsd022_xsd.xsd022 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    child1_or_child2=[
        [
            "123456",
            "abcdef",
            "xxxxxxxx",
        ],
        DerivedElement(
            qname="{http://foo.com}child2",
            value=True
        ),
        DerivedElement(
            qname="{http://foo.com}child2",
            value=False
        ),
        DerivedElement(
            qname="{http://foo.com}child2",
            value=False
        ),
        DerivedElement(
            qname="{http://foo.com}child2",
            value=True
        ),
        DerivedElement(
            qname="{http://foo.com}child2",
            value="abcdef"
        ),
        DerivedElement(
            qname="{http://foo.com}child2",
            value="xxxxxxxx"
        ),
    ]
)
