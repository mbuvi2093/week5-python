# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Subclass 1
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, android_version):
        super().__init__(brand, model, storage)
        self.android_version = android_version

    def specs(self):
        super().specs()
        print(f"Android Version: {self.android_version}")

    def use_google_assistant(self):
        print(f"{self.model} is launching Google Assistant 🤖")

# Subclass 2
class iPhone(Smartphone):
    def __init__(self, brand, model, storage, ios_version):
        super().__init__(brand, model, storage)
        self.ios_version = ios_version

    def specs(self):
        super().specs()
        print(f"iOS Version: {self.ios_version}")

    def use_siri(self):
        print(f"{self.model} is launching Siri 🍎")

# Creating objects
phone1 = AndroidPhone("Samsung", "Galaxy S23", 256, "Android 13")
phone2 = iPhone("Apple", "iPhone 15", 512, "iOS 17")

# Using methods
phone1.specs()
phone1.use_google_assistant()
phone1.call("0721507436")

print()  # Just spacing

phone2.specs()
phone2.use_siri()
phone2.call("0758937100")
