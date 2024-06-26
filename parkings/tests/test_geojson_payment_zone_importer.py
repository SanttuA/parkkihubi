import os

from parkings.importers import PaymentZoneImporter

mydir = os.path.dirname(__file__)


def test_payment_zone_importer():
    filename = os.path.join(mydir, 'geojson_payment_zones_importer_data.geojson')
    importer = PaymentZoneImporter()
    data = importer.read_and_parse(filename)
    payment_zone = next(iter(data))

    assert payment_zone['name'] == "Zone 1"
    assert payment_zone['number'] == 0
    assert payment_zone['geom'].wkt == (
        'MULTIPOLYGON (('
        '(-47.900390625 -14.944784875088372, -51.591796875 -19.91138351415555, -41.11083984375'
        ' -21.309846141087192, -43.39599609375 -15.390135715305204, -47.900390625 -14.944784875088372), '
        '(-46.6259765625 -17.14079039331664, -47.548828125 -16.804541076383455, -46.23046874999999'
        ' -16.699340234594537, -45.3515625 -19.31114335506464, -46.6259765625 -17.14079039331664), '
        '(-44.40673828125 -18.375379094031825, -44.4287109375 -20.097206227083888, -42.9345703125'
        ' -18.979025953255267, -43.52783203125 -17.602139123350838, -44.40673828125 -18.375379094031825)))'
    )
