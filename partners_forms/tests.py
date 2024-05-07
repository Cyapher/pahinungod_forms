from django.test import TestCase
from .models import Type, Partner, File
from faker import Faker
import timeit

class PartnerCRUDTests(TestCase):
    def setUp(self):
        # Create a Faker instance
        self.fake = Faker()

    def test_partner_create_read_update_delete(self):
        def test_function():
            # Test partner creation
            partner = Partner.objects.create(
                partner_name=self.fake.company(),
                partnership_extension=self.fake.random_element(elements=['Health Training: Basic Life Support', 'Health Training: Breast Advocacy and PFA']),
                stakeholder_category=self.fake.random_element(elements=['Private', 'Government']),
                second_category=self.fake.random_element(elements=['NGO', 'Company']),
                other_choice='',
                Agreement_Start_Date=self.fake.date_between(start_date='-1y', end_date='today'),
                Agreement_End_Date=self.fake.date_between(start_date='today', end_date='+1y')
            )

            # Test that partner was created successfully
            self.assertIsNotNone(partner)

            # Test file creation for the partner
            file = File.objects.create(
                file_field=self.fake.file_path(),  # Assuming you have a method to generate file paths
                partner=partner
            )

            # Test that the file was created and attached to the partner
            self.assertEqual(File.objects.filter(partner=partner).count(), 1)

            # Test partner reading
            partner = Partner.objects.get(pk=partner.pk)
            self.assertIsNotNone(partner)

            # Test partner updating
            partner.partner_name = self.fake.company()
            # partner.save()
            updated_partner = Partner.objects.get(pk=partner.pk)
            self.assertNotEqual(updated_partner.partner_name, partner.partner_name)

            # Test file deletion
            file_count_before_delete = File.objects.count()
            file.delete()
            self.assertEqual(File.objects.count(), file_count_before_delete - 1)

            # Test partner deletion
            partner.delete()
            self.assertFalse(Partner.objects.filter(pk=partner.pk).exists())

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
