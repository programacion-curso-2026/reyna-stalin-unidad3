from mecanico import Mecanico
from database import Database
from mecanico_dao import MecanicoDAO

database = Database()
mecanico_dao = MecanicoDAO(database)
mecanico_1 = Mecanico("David Guevara", "0992848484", "Via a la Costa", "Popular Mechanics with IA", 100)

mecanico_2 = Mecanico("Juan Perez", "0992848484", "Alborada", "Microservos", 120)