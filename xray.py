#test
from procedure import Procedure

class Xray (Procedure):
    """A procedure that photographs the patient using X-rays."""

    def __init__ (self, type, result, name, patient, description, xray_type):
        # This function allows the subclass to inherit all the methods and attributes of the superclass.
        super().__init__(type, result, name, patient, description,)
        self.xray_type = xray_type                                   # This is the type of the x-ray (e.g., dental, bone, abdominal)

    def perform (self):                                              # This will show that the Vet will perform the X-ray and its type.
        print (f"{self.name} will now perform {self.xray_type} {self.type}.")

    def add_results(self, result):                                   # This will add and update the result of the X-ray.
        self.result.update(result)
        print(f"{self.type} results is now available.\n")

    def release_results(self):                                       # This will show the results of the X-ray.
        print(f"{self.xray_type} X-ray Report:")
        for key, value in self.result.items():                       # This is a loop that prints out each key and its value in the dictionary.
            print(f"{key}: {value}")
