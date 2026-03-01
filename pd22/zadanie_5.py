from faker import Faker

def main():
    fake = Faker("pl_PL")

    print("I 10 losowych polskich imion i nazwisk:\n")
    for i in range(10):
        print(f"{i+1}. {fake.first_name()} {fake.last_name()}")

    print("\nII 10 losowych zdań:\n")
    for i in range(10):
        print(f"{i+1}. {fake.sentence()}")

if __name__ == "__main__":
    main()