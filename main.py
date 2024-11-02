#task1
class Human:
    def __init__(self, name, age, city, work_experience, skills):
        self.name = name
        self.age = age
        self.city = city
        self.work_experience = work_experience
        self.skills = skills

    def getInfo(self):
        return (f"\nName: {self.name};"
                f"\nAge: {self.age};"
                f"\nCity: {self.city};"
                f"\nWork experience: {self.work_experience};"
                f"\nSkills: {self.skills}")
class Builder(Human):
    def __init__(self,name, age, city, work_experience, skills, forklift_license):
        super().__init__(name, age, city, work_experience, skills)
        self.forklift_license = forklift_license

    def getInfo(self):
        return f"{super().getInfo()}; \nForklift license availability: {self.forklift_license}"

class Sailor(Human):
    def __init__(self, name, age, city, work_experience, skills, vessel_type):
        super().__init__(name, age, city, work_experience, skills)
        self.vessel_type = vessel_type

    def getInfo(self):
        return f"{super().getInfo()}; \nVessel type: {self.vessel_type}"


class Pilot(Human):
    def __init__(self, name, age, city, work_experience, skills, aircraft_type):
        super().__init__(name, age, city, work_experience, skills)
        self.aircraft_type = aircraft_type

    def getInfo(self):
        return f"{super().getInfo()}; \nAircraft type: {self.aircraft_type}"

firstPerson = Builder("Stiv", 36, "Miami, Florida", "10 years", "Tiler", "Yes")
print(firstPerson.getInfo())
sailor = Sailor("Jack", 29, "Covington, Georgia", "5 years", "Navigator", "Cargo ship")
print(sailor.getInfo())
pilot = Pilot("Anna", 42, "Forks, Washington", "15 years", "Jet pilot", "Commercial airplane")
print(pilot.getInfo())

#task2
class Passport:
    def __init__(self, full_name, birth_date, passport_number, nationality):
        self.full_name = full_name
        self.birth_date = birth_date
        self.passport_number = passport_number
        self.nationality = nationality

    def get_info(self):
        return (f"Full Name: {self.full_name}\n"
                f"Birth Date: {self.birth_date}\n"
                f"Passport Number: {self.passport_number}\n"
                f"Nationality: {self.nationality}")


class ForeignPassport(Passport):
    def __init__(self, full_name, birth_date, passport_number, nationality, foreign_passport_number, visas):
        super().__init__(full_name, birth_date, passport_number, nationality)
        self.foreign_passport_number = foreign_passport_number
        self.visas = visas

    def get_info(self):
        base_info = super().get_info()
        visas_info = "\nVisas: " + ", ".join(self.visas) if self.visas else "No visas"
        return (f"{base_info}\n"
                f"Foreign Passport Number: {self.foreign_passport_number}\n"
                f"{visas_info}")

passport = Passport("Ivan Ivanchenko", "1990-01-01", "AB123456", "Ukrainian")
print("Passport Info:")
print(passport.get_info())

foreign_passport = ForeignPassport("Ivan Ivanchenko", "1990-01-01", "AB123456", "Ukrainian", "FP789012", ["USA", "Canada", "Germany"])
print("\nForeign Passport Info:")
print(foreign_passport.get_info())
