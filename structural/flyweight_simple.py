import logging

logging.basicConfig(level='INFO')

class ComplexCars(object):
    """Separate class for Complex Cars."""
 
    def __init__(self):
        pass
 
    def cars(self, car_name):
        return "ComplexPattern[% s]" % (car_name)
 
class CarFamilies(object):
    """Dictionary to store ids of the car."""
 
    car_family = {}
 
    def __new__(cls, name, car_family_id):
        try:
            id = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.car_family[car_family_id] = id
        return id
 
    def set_car_info(self, car_info):
        """Set the car information."""
        cg = ComplexCars()
        self.car_info = cg.cars(car_info)
 
    def get_car_info(self):
        """Return the car information."""
        return (self.car_info)

def main() -> None:
    car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi'))
    car_family_objects = []

    for i in car_data:
        obj = CarFamilies(i[0], i[1])
        obj.set_car_info(i[2])
        car_family_objects.append(obj)
 
    # Similar id's says that they are same objects
    for i in car_family_objects:
        logging.info("id = " + str(id(i)))
        logging.info(i.get_car_info())


if __name__ == '__main__':
    main()
