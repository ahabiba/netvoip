from django.test import TestCase
from pay.models import Carrier,RateDeck,Suppliers_Query
from django.utils import timezone



#model test Carrier
class Carrier_Test(TestCase):

    def create_carrier(self,nameid='AAT',descriptions='ALL access telecom',rate='6s'):
        return Carrier.objects.create(nameid=nameid,description=descriptions,rate=rate)

    def test_carrier_creation(self):
        carrier = self.create_carrier()
        self.assertTrue(isinstance(carrier,Carrier))
        self.assertEqual(carrier.__str__(),carrier.nameid)

class Ratedeck_Test(TestCase):
    def create_carrier(self,nameid='AAT',descriptions='ALL access telecom',rate='6s'):
        return Carrier.objects.create(nameid=nameid,description=descriptions,rate=rate)

    def create_ratedeck(self):
        carrier = self.create_carrier()
        return RateDeck.objects.create(carrier=carrier,uploadday=timezone.now(),efectiveday=timezone.now())

    def test_ratedeck_creation(self):
        ratedeck = self.create_ratedeck()
        self.assertTrue(isinstance(ratedeck,RateDeck))
        self.assertEqual(ratedeck.carrier.nameid,ratedeck.carrier.__str__())

class Supplier_Test(TestCase):

    def test_supplier(self):
        Supplier = Suppliers_Query()
        Supplier.GetSuppliers(tenant='netprovidersolutions',ID='INTER',Time='2019-06-03T11:04:05Z',Account='aat',Destinations='1407919')
        self.assertEqual(Supplier.profileid,'INTER')