from Address import Address
from Mailing import Mailing


to_address = Address("569542", "Omsk", "Shishova", 33, "11")
from_address = Address("456256", "Msk", "cvetochnaya", 78, "55")

action = Mailing(from_address, to_address, 33, "Н787ГГ789")

action.res()
