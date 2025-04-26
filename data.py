
dog_pets = [
    Pet(
        id=uuid4(),
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        sex=Sex.MALE,
        age=3,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.LARGE,
            temperament=Temperament.LOYAL,
            fur_type=FurType.LONG,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Golden Retriever",
            species="Dog",
            hypoallergenic="N",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Bella",
        species="Dog",
        breed="Poodle",
        sex=Sex.FEMALE,
        age=2,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.MEDIUM,
            temperament=Temperament.SMART,
            fur_type=FurType.CURLY,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.HIGH,
            breed="Poodle",
            species="Dog",
            hypoallergenic="Y",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Charlie",
        species="Dog",
        breed="Beagle",
        sex=Sex.MALE,
        age=4,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.MEDIUM,
            temperament=Temperament.CURIOUS,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Beagle",
            species="Dog",
            hypoallergenic="N",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Lucy",
        species="Dog",
        breed="Shih Tzu",
        sex=Sex.FEMALE,
        age=5,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.LOW,
            size=Size.SMALL,
            temperament=Temperament.AFFECTIONATE,
            fur_type=FurType.LONG,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.HIGH,
            breed="Shih Tzu",
            species="Dog",
            hypoallergenic="Y",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Max",
        species="Dog",
        breed="German Shepherd",
        sex=Sex.MALE,
        age=3,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.LARGE,
            temperament=Temperament.ATHLETIC,
            fur_type=FurType.MEDIUM,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="German Shepherd",
            species="Dog",
            hypoallergenic="N",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Daisy",
        species="Dog",
        breed="Bulldog",
        sex=Sex.FEMALE,
        age=4,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.LOW,
            size=Size.MEDIUM,
            temperament=Temperament.CALM,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.LOW,
            breed="Bulldog",
            species="Dog",
            hypoallergenic="N",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Milo",
        species="Dog",
        breed="Chihuahua",
        sex=Sex.MALE,
        age=2,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.EXCITABLE,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.LOW,
            breed="Chihuahua",
            species="Dog",
            hypoallergenic="N",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Luna",
        species="Dog",
        breed="Labrador Retriever",
        sex=Sex.FEMALE,
        age=3,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.LARGE,
            temperament=Temperament.PLAYFUL,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Labrador Retriever",
            species="Dog",
            hypoallergenic="N",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Rocky",
        species="Dog",
        breed="Boxer",
        sex=Sex.MALE,
        age=5,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.LARGE,
            temperament=Temperament.ATHLETIC,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Boxer",
            species="Dog",
            hypoallergenic="N",
        ),
    ),
    Pet(
        id=uuid4(),
        name="Sadie",
        species="Dog",
        breed="Cocker Spaniel",
        sex=Sex.FEMALE,
        age=4,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.MEDIUM,
            temperament=Temperament.HAPPY,
            fur_type=FurType.MEDIUM,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Cocker Spaniel",
            species="Dog",
            hypoallergenic="N",
        ),
    ),
]


pets1 = [
    Pet(
        id=uuid4(),
        name="Bella",
        species="Dog",
        breed="Chihuahua",
        sex=Sex.FEMALE,
        age=2,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.CURIOUS,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.LOW,
            breed="Chihuahua",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Max",
        species="Dog",
        breed="Pomeranian",
        sex=Sex.MALE,
        age=3,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.SMALL,
            temperament=Temperament.PLAYFUL,
            fur_type=FurType.LONG,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.HIGH,
            breed="Pomeranian",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Daisy",
        species="Dog",
        breed="Yorkshire Terrier",
        sex=Sex.FEMALE,
        age=1,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.LOYAL,
            fur_type=FurType.MEDIUM,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.HIGH,
            breed="Yorkshire Terrier",
            species="Dog",
            hypoallergenic="Y"
        )
    ),
    Pet(
        id=uuid4(),
        name="Charlie",
        species="Dog",
        breed="Shih Tzu",
        sex=Sex.MALE,
        age=4,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.LOW,
            size=Size.SMALL,
            temperament=Temperament.CALM,
            fur_type=FurType.LONG,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.HIGH,
            breed="Shih Tzu",
            species="Dog",
            hypoallergenic="Y"
        )
    ),
    Pet(
        id=uuid4(),
        name="Luna",
        species="Dog",
        breed="Maltese",
        sex=Sex.FEMALE,
        age=2,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.AFFECTIONATE,
            fur_type=FurType.LONG,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.HIGH,
            breed="Maltese",
            species="Dog",
            hypoallergenic="Y"
        )
    ),
    Pet(
        id=uuid4(),
        name="Rocky",
        species="Dog",
        breed="Toy Poodle",
        sex=Sex.MALE,
        age=5,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.SMALL,
            temperament=Temperament.SMART,
            fur_type=FurType.CURLY,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Toy Poodle",
            species="Dog",
            hypoallergenic="Y"
        )
    ),
    Pet(
        id=uuid4(),
        name="Lola",
        species="Dog",
        breed="Pekingese",
        sex=Sex.FEMALE,
        age=6,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.LOW,
            size=Size.SMALL,
            temperament=Temperament.ASSERTIVE,
            fur_type=FurType.LONG,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.HIGH,
            breed="Pekingese",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Milo",
        species="Dog",
        breed="French Bulldog",
        sex=Sex.MALE,
        age=2,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.FUNNY,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="French Bulldog",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Zoe",
        species="Dog",
        breed="Papillon",
        sex=Sex.FEMALE,
        age=1,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.SMALL,
            temperament=Temperament.CURIOUS,
            fur_type=FurType.MEDIUM,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Papillon",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Cooper",
        species="Dog",
        breed="Miniature Schnauzer",
        sex=Sex.MALE,
        age=4,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.LOYAL,
            fur_type=FurType.MEDIUM,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Miniature Schnauzer",
            species="Dog",
            hypoallergenic="Y"
        )
    ),
]
pets5 = [
    Pet(
        id=uuid4(),
        name="Buddy",
        species="Dog",
        breed="Chihuahua",
        sex=Sex.MALE,
        age=2,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.LOYAL,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.LOW,
            breed="Chihuahua",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Luna",
        species="Dog",
        breed="Xoloitzcuintli",
        sex=Sex.FEMALE,
        age=3,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.LOW,
            size=Size.MEDIUM,
            temperament=Temperament.CALM,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.LOW,
            breed="Xoloitzcuintli",
            species="Dog",
            hypoallergenic="Y"
        )
    ),
    Pet(
        id=uuid4(),
        name="Max",
        species="Dog",
        breed="American Eskimo Dog",
        sex=Sex.MALE,
        age=4,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.MEDIUM,
            temperament=Temperament.PLAYFUL,
            fur_type=FurType.LONG,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.HIGH,
            breed="American Eskimo Dog",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Daisy",
        species="Dog",
        breed="American Pit Bull Terrier",
        sex=Sex.FEMALE,
        age=2,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.MEDIUM,
            temperament=Temperament.AFFECTIONATE,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="American Pit Bull Terrier",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Rocky",
        species="Dog",
        breed="American Bulldog",
        sex=Sex.MALE,
        age=5,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.LARGE,
            temperament=Temperament.ASSERTIVE,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="American Bulldog",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Bella",
        species="Dog",
        breed="Boston Terrier",
        sex=Sex.FEMALE,
        age=1,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.SMART,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.LOW,
            breed="Boston Terrier",
            species="Dog",
            hypoallergenic="Y"
        )
    ),
    Pet(
        id=uuid4(),
        name="Shadow",
        species="Dog",
        breed="Alaskan Malamute",
        sex=Sex.MALE,
        age=6,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.LARGE,
            temperament=Temperament.ATHLETIC,
            fur_type=FurType.LONG,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.HIGH,
            breed="Alaskan Malamute",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Ruby",
        species="Dog",
        breed="Australian Shepherd",
        sex=Sex.FEMALE,
        age=2,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.MEDIUM,
            temperament=Temperament.CURIOUS,
            fur_type=FurType.MEDIUM,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Australian Shepherd",
            species="Dog",
            hypoallergenic="N"
        )
    ),
    Pet(
        id=uuid4(),
        name="Oliver",
        species="Dog",
        breed="American Hairless Terrier",
        sex=Sex.MALE,
        age=3,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.MEDIUM,
            size=Size.SMALL,
            temperament=Temperament.FUNNY,
            fur_type=None,
            intelligence=IntelligenceLevel.MEDIUM,
            maintenance=MaintenanceLevel.LOW,
            breed="American Hairless Terrier",
            species="Dog",
            hypoallergenic="Y"
        )
    ),
    Pet(
        id=uuid4(),
        name="Nala",
        species="Dog",
        breed="Catahoula Leopard Dog",
        sex=Sex.FEMALE,
        age=4,
        petChar=PetCharacteristic(
            activity_level=ActivityLevel.HIGH,
            size=Size.LARGE,
            temperament=Temperament.EXCITABLE,
            fur_type=FurType.SHORT,
            intelligence=IntelligenceLevel.HIGH,
            maintenance=MaintenanceLevel.MEDIUM,
            breed="Catahoula Leopard Dog",
            species="Dog",
            hypoallergenic="N"
        )
    ),
]


# Example valid email addresses
contact_info_1 = ContactInfo(
    email="john.doe@example.com",
    phone="555-123-4567",
    address=Address(
        address1="123 Main St",
        address2="Apt 4B",
        city="Madison",
        state="WI",
        postcode="53703",
        country="USA"
    )
)

contact_info_2 = ContactInfo(
    email="jane.smith@example.com",
    phone="555-234-5678",
    address=Address(
        address1="456 Oak St",
        address2=None,
        city="Milwaukee",
        state="WI",
        postcode="53202",
        country="USA"
    )
)

contact_info_3 = ContactInfo(
    email="mike.jones@example.com",
    phone="555-345-6789",
    address=Address(
        address1="789 Pine St",
        address2="Suite 202",
        city="Green Bay",
        state="WI",
        postcode="54301",
        country="USA"
    )
)

contact_info_4 = ContactInfo(
    email="lisa.white@example.com",
    phone="555-456-7890",
    address=Address(
        address1="101 Maple St",
        address2=None,
        city="Appleton",
        state="WI",
        postcode="54911",
        country="USA"
    )
)

contact_info_5 = ContactInfo(
    email="james.black@example.com",
    phone="555-567-8901",
    address=Address(
        address1="202 Birch St",
        address2="Unit 3C",
        city="Kenosha",
        state="WI",
        postcode="53140",
        country="USA"
    )
)
# Function to generate example offerings
def generate_offerings(pets: List[Pet]) -> List[Offering]:
    offerings = []
    

    
    for i in range(len(pets)):
        # Randomly select a pet
        pet = pets[i]
        
        # Generate a random price and availability
        price = round(uniform(50.0, 500.0), 2)  # Random price between $50 and $500
        availability = Availability.AVAILABLE  # For simplicity, assuming all are available
        
        # Create and append the offering
        offering = Offering(price=price, pet=pet, availability=availability)
        offerings.append(offering)
    
    return offerings

# Example: Generate 5 offerings
offerings1 = generate_offerings(pets1)
# offerings2 = generate_offerings(pets2)
offerings3 = generate_offerings(pets3)
offerings4 = generate_offerings(pets4)
offerings2 = generate_offerings(pets5)

v1 = Vendor(name="bobs pets",contactInfo=contact_info_1,offerings=offerings1)
v2 = Vendor(name="jamies pets",contactInfo=contact_info_2,offerings=offerings2)
v3 = Vendor(name="Olivia's Orangitans",contactInfo=contact_info_3,offerings=offerings3)
v4 = Vendor(name="Monty's Pythons",contactInfo=contact_info_3,offerings=offerings4)