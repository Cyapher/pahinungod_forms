from django.test import TestCase
from django.urls import reverse
from .models import Volunteer, Program
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from faker import Faker
import timeit

User = get_user_model()

class VolunteerProgramCRUDTests(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password')

    def test_volunteer_create_read_update_delete(self):
        def test_function():
            # Test volunteer creation

            # Create a program
            self.program = Program.objects.create(
                code=Faker().lexify(text='???###'),  # Random code like ABC123
                name=Faker().sentence(nb_words=4),   # Random name like "Test Program Name"
                description=Faker().paragraph()      # Random description
        )

            volunteer = Volunteer.objects.create_user(
                username=Faker().user_name(),           # Random username
                email=Faker().email(),                  # Random email
                password=Faker().password(),            # Random password
                middle_name=Faker().first_name(),       # Random middle name
                address=Faker().address(),              # Random address
                mobile=Faker().phone_number(),          # Random phone number
                telephone=Faker().phone_number(),       # Random phone number
                birthdate=Faker().date_of_birth(),      # Random birthdate
                civilStatus=Faker().random_element(elements=('Single', 'Married')),  # Random civil status
                sex=Faker().random_element(elements=('Male', 'Female', 'Other/Will not disclose')),  # Random sex
                bloodType=Faker().random_element(elements=('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')),  # Random blood type
                religion=Faker().word(),                # Random religion
                healthConditions=Faker().sentence(),    # Random health conditions
                skillsHobbies=Faker().sentence(),       # Random skills/hobbies
                foodRestrictions=Faker().sentence(),    # Random food restrictions
                constituentUnit=Faker().word(),         # Random constituent unit
                specification=Faker().word(),           # Random specification
                occupation=Faker().random_element(elements=('Physician', 'Nurse', 'Pharmacist', 'Dentist', 'ENT', 'Teacher', 'Other')),  # Random occupation
                otherOccu=Faker().word(),               # Random other occupation
                beneficiaries=Faker().name(),           # Random beneficiaries
                relation=Faker().word(),                # Random relation
                contactNum=Faker().phone_number(),      # Random contact number
                contactEmail=Faker().email(),           # Random contact email
                prcLicense=Faker().random_number(digits=7),  # Random PRC license number
                dept=Faker().word(),                    # Random department
                company=Faker().company(),              # Random company
                officeAdd=Faker().address(),            # Random office address
                license_telephone=Faker().phone_number(),  # Random license telephone
                license_email=Faker().email(),          # Random license email
                workSched=Faker().sentence(),           # Random work schedule
                idNum=Faker().random_number(digits=5),  # Random ID number
                course=Faker().sentence(),              # Random course
                college=Faker().sentence(),             # Random college
                yearLvl=Faker().random_element(elements=('1', '2', '3', '4', '5')),  # Random year level
                startDate=Faker().random_element(elements=('immediately', 'next_week', 'next_month', 'Other')),  # Random start date
                alumnusCheck=Faker().boolean(),         # Random boolean value
                pghCheck=Faker().boolean(),             # Random boolean value
                workCheck=Faker().boolean(),            # Random boolean value
                licenseCheck=Faker().boolean(),         # Random boolean value
                studentCheck=Faker().boolean()          # Random boolean value
            )

            # Add program to volunteer
            volunteer.programs.set([self.program])
            self.assertEqual(volunteer.programs.count(), 1)

            # Test program creation
            self.assertEqual(Program.objects.count(), 1)

            # Test volunteer reading
            volunteer = Volunteer.objects.get(username=volunteer.username)
            self.assertIsNotNone(volunteer)

            # Test volunteer updating
            volunteer.middle_name = Faker().first_name()  # Update middle name with a new random value
            updated_volunteer = Volunteer.objects.get(username=volunteer.username)
            self.assertNotEqual(updated_volunteer.middle_name, volunteer.middle_name)

            # Test program update
            self.program.name = Faker().sentence(nb_words=4)  # Update name with a new random value
            updated_program = Program.objects.get(code=self.program.code)
            self.assertNotEqual(updated_program.name, self.program.name)

            volunteer = Volunteer.objects.get(username=volunteer.username)
            self.assertIsNotNone(volunteer)

            # Test volunteer deletion
            volunteer.delete()
            self.assertEqual(Volunteer.objects.count(), 1)

            # Test program deletion
            self.program.delete()
            self.assertEqual(Program.objects.count(), 0)

        # Number of times to run the test function
        num_iterations = 5

        # Measure elapsed time for each iteration
        elapsed_times = []
        for _ in range(num_iterations):
            start_time = timeit.default_timer()
            test_function()
            end_time = timeit.default_timer()
            elapsed_times.append(end_time - start_time)

        # Calculate average elapsed time
        average_elapsed_time = "{:.2f}".format(sum(elapsed_times) / num_iterations)
        print(f"Average elapsed time for {num_iterations} iterations: {average_elapsed_time} seconds")
