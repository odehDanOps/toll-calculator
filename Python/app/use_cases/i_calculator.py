from abc import ABCMeta, abstractmethod

class ICalculator(metaclass=ABCMeta):

	@abstractmethod
	def get_toll_fee(self, vehicle, vehicle_number):
		raise NotImplementedError()