from output.models.ms_data.wildcards.wild_g013_xsd.wild_g013 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    target_namespace_w3_org_1999_xhtml_element=[
        AnyElement(
            qname="{http://www.w3.org/1999/xhtml}foo",
            text="foo bar"
        ),
        AnyElement(
            qname="{http://xsdtesting}b",
            text="testing"
        ),
        AnyElement(
            qname="{http://www.w3.org/1999/xhtml}foo",
            text="foo bar"
        ),
        AnyElement(
            qname="{http://www.w3.org/1999/xhtml}foo",
            text="foo bar"
        ),
        AnyElement(
            qname="{http://xsdtesting}b",
            text="testing"
        ),
        AnyElement(
            qname="{http://xsdtesting}b",
            text="testing"
        ),
    ]
)
