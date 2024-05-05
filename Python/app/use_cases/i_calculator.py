from abc import ABCMeta, abstractmethod

class ICalculator(metaclass=ABCMeta):

	@abstractmethod
	def get_vehicle_toll_fee(self, vehicle: str, vehicle_number: str):
		raise NotImplementedError()