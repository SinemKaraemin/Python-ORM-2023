import os
import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name: str, species: str):
    pet = Pet.objects.create(name=name, species=species,)

    return f"{pet.name} is a very cute {pet.species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        age=age,
        origin=origin,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()

# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
#
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))


def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(l) for l in locations)


def new_capital() -> None:
    # Location.objects.filter(pk=1).update(is_capital=True)

    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        percentage_off = sum(int(x) for x in str(car.year)) / 100
        discount = float(car.price) * percentage_off
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


# apply_discount()
# print(get_recent_cars())


def show_unfinished_tasks() -> str:
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return '\n'.join(str(t) for t in unfinished_tasks)


def complete_odd_tasks() -> None:
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(x) - 3) for x in text)

    # Task.objects.filter(title=task_title).update(description=decoded_text)

    tasks_with_matching_title = Task.objects.filter(title=task_title)
    decoded_text = ''.join(chr(ord(x) - 3) for x in text)

    for task in tasks_with_matching_title:
        task.description = decoded_text
        task.save()


# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title='Simple Task') .description)


def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_id_deluxe_rooms = []

    for room in deluxe_rooms:
        if room.id % 2 == 0:
            even_id_deluxe_rooms.append(str(room))

    return '\n'.join(even_id_deluxe_rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by("id")

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()

    if last_room.is_reserved:
        last_room.delete()


# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=101).is_reserved)


def update_characters():
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty",
    )


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + " " + second_character.name
    fusion_level = (first_character.level + second_character.level) // 2
    fusion_class = "Fusion"
    fusion_strength = (first_character.strength + second_character.strength) * 1.2
    fusion_dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    fusion_intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    fusion_hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ["Mage", "Scout"]:
        fusion_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        fusion_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=fusion_name,
        class_name=fusion_class,
        level=fusion_level,
        strength=fusion_strength,
        dexterity=fusion_dexterity,
        intelligence=fusion_intelligence,
        hit_points=fusion_hit_points,
        inventory=fusion_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()


# character1 = Character.objects.create(
#     name="Gandalf",
#     class_name="Mage",
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory="Staff of Magic, Spellbook",
# )
#
# character2 = Character.objects.create(
#     name="Hector",
#     class_name="Warrior",
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory="Sword of Troy, Shield of Protection",
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)

