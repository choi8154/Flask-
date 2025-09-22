from faker import Faker

fake = Faker("ko-kr")

users = []
for i in range(50):
    users.append({"name":fake.name(), "phone":fake.phone_number(), "email":fake.email()})

for user in users:
    print(user)