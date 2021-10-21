from django.test import TestCase
from django.core.exceptions import ValidationError
from WEB_SERVER.models import Device, Type, Data, Command, Button, Source_Device
from django.conf import settings

from django.core.files.uploadedfile import SimpleUploadedFile
from AUTH_SYSTEM.models import New_User

User = New_User


class TypeTestCase(TestCase):
    def setUp(self) -> None:
        name = 'Light'
        new_type = Type(name)
        new_type.save()
        new_type.full_clean()
        return super().setUp()

    def test_valid_name_type(self):
        invalid_name = [
            'KardenIR',
            "Light2",
            "Cooler",
        ]
        for name in invalid_name:
            new_type = Type(name)
            new_type.full_clean()
            new_type.save()
            self.assertIsInstance(new_type, Type)

    def test_invalid_name_type_error(self):
        invalid_name = [
            'Karden-IR',
            'Karden IR',
            "Light*",
            "Cooler!",
        ]
        for name in invalid_name:
            with self.assertRaises(ValidationError):
                new_type = Type(name)
                new_type.full_clean()

    def test_exist_type_error(self):
        exist_name = 'Light'
        with self.assertRaises(ValidationError):
            new_type = Type(exist_name)
            new_type.full_clean()

    def test_longer_len_name_error(self):
        max_len = 62
        name = 'A' * (max_len + 1)
        with self.assertRaises(ValidationError):
            new_type = Type(name)
            new_type.full_clean()

    def test_blank_name_error(self):
        name = ''
        with self.assertRaises(ValidationError):
            new_type = Type(name)
            new_type.full_clean()


class DeviceTestCase(TestCase):
    def setUp(self) -> None:
        new_type = Type('NewLight')
        new_type.save()
        self.user = User.objects.create(username='nova')

        self.type = new_type
        self.name = 'Light room2'
        self.ip = '127.0.0.1'
        self.password = 'supernova'
        self.mac = '192.0.0.1'
        self.description = 'example description'
        self.status = True
        return super().setUp()

    def test_make_new_device(self):
        device = Device(type=self.type,
                        name=self.name,
                        user=self.user,
                        ip=self.ip,
                        password=self.password,
                        mac=self.mac,
                        description=self.description,
                        status=self.status)
        device.full_clean()
        device.save()
        self.assertIsInstance(device, Device)

    def test_make_new_device_wiht_long_len(self):
        max_len_ip = 64
        max_len_password = 62
        max_len_mac = 17
        max_len_description = 600
        max_len_name = 36

        name = 'x' * (max_len_name + 1)
        ip = 'x' * (max_len_ip + 1)
        password = 'x' * (max_len_password + 1)
        mac = 'x' * (max_len_mac + 1)
        description = 'x' * (max_len_description + 1)
        with self.assertRaises(ValidationError):
            device = Device(type=self.type,
                            name=name,
                            user=self.user,
                            ip=ip,
                            password=password,
                            mac=mac,
                            description=description,
                            status=self.status)
            device.full_clean()
            device.save()


class DataTestCase(TestCase):
    def setUp(self) -> None:
        new_type = Type('NewLight')
        new_type.save()
        user = User.objects.create(username='nova')
        type = new_type
        status = True
        name = 'Light room2'
        self.device = Device(user=user, type=type, name=name, status=status)
        self.device.save()
        self.data = ["{'log': 'value'}", {'log': 'value'}]

        return super().setUp()

    def test_make_new_data(self):
        for data in self.data:
            new_data = Data(device=self.device, data=data)
            new_data.full_clean()
            new_data.save()
            self.assertIsInstance(new_data, Data)


class CommandTestCase(TestCase):
    def setUp(self) -> None:
        new_type = Type('NewLight')
        new_type.save()
        user = User.objects.create(username='nova')
        type = new_type
        status = True
        name = 'Light room2'
        self.device = Device(user=user, type=type, name=name, status=status)
        self.device.save()
        self.command_data = {'updata': 'link update'}
        return super().setUp()

    def test_make_new_command(self):
        command = Command(device=self.device,
                          data=self.command_data,
                          complated=True)
        command.full_clean()
        command.save()
        self.assertIsInstance(command, Command)

    def test_make_new_command_2(self):
        command = Command(device=self.device,
                          data={'destroy': None},
                          complated=True)
        command.full_clean()
        command.save()
        self.assertIsInstance(command, Command)

    def test_make_new_command_with_send_command_to_device(self):
        command = Command(device=self.device,
                          data=self.command_data,
                          complated=False)
        command.full_clean()
        command.save()
        self.assertIsInstance(command, Command)


class ButtonTestCase(TestCase):
    def setUp(self) -> None:
        new_type = Type('NewLight')
        new_type.save()
        user = User.objects.create(username='nova')
        type = new_type
        status = True
        name = 'Light room2'
        self.device = Device(user=user, type=type, name=name, status=status)
        self.device.save()
        self.name = 'OFF'
        self.control_name = 'Cooler'
        self.array = """72,9000,600,660,5457,649,7676,645,6466,
        946,4676,649,9467,6464,967,9000,600,660,5457,649,7676,
        645,6466,946,4676,649,9467,6464,967,9000,600,660,5457,649
        ,7676,645,6466,946,4676,649,9467,6464,967,9000,600,660,5457,
        649,7676,645,6466,946,4676,649,9467,6464,967,9000,600,660,5457,
        649,7676,645,6466,946,4676,649,9467,6464,967,9000,600,660,5457
        ,649,7676,645,6466,946,4676,649,9467,6464,967,9000,600,660,5457,
        649,7676,645,6466,946,4676,649,9467,6464,967,9000,600,660,5457,649,
        7676,645,6466,946,4676,649,9467,6464,967,9000,600,660,5457,649,7676,
        645,6466,946,4676,649,9467,6464,967"""
        self.is_star = True
        return super().setUp()

    def test_make_new_button(self):
        new_button = Button(device=self.device,
                            name=self.name,
                            control_name=self.control_name,
                            array=self.array,
                            is_star=self.is_star)
        new_button.full_clean()
        new_button.save()
        self.assertIsInstance(new_button, Button)

    def test_make_new_button_with_long_len(self):
        max_len_control_name = 80
        max_len_name = 80

        control_name = 'x' * (max_len_control_name + 1)
        name = 'x' * (max_len_name + 1)
        with self.assertRaises(ValidationError):
            new_button = Button(device=self.device,
                                name=name,
                                control_name=control_name,
                                array=self.array,
                                is_star=self.is_star)
            new_button.full_clean()
            new_button.save()


class SourceDeviceTestCase(TestCase):
    def setUp(self) -> None:
        self.type = Type('NewLight')
        self.type.save()

        self.file = SimpleUploadedFile('Source-File.bin',
                                       b'my source device version 0.2')
        self.vesrion = '0.2'
        return super().setUp()

    def test_make_new_source(self):
        new_source = Source_Device(type=self.type,
                                   version=self.vesrion,
                                   source=self.file)
        new_source.full_clean()
        new_source.save()