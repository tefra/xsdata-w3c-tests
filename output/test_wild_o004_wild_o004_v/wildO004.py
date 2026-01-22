from output.models.ms_data.wildcards.wild_o004_xsd.wild_o004 import Foo


obj = Foo(
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://foobar wildO004.xsd http://foo wildO004a.xsd',
        '{http://foo}name': 'bar',
    }
)
