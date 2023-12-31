import random
from dataclasses import dataclass, field
from typing import TypeAlias, TypedDict

from faker import Faker

T_GROUP_NAME: TypeAlias = str
T_GROUP_NAMES: TypeAlias = list[T_GROUP_NAME]


class Human(TypedDict):
    name: str
    group: T_GROUP_NAME


T_HUMANS: TypeAlias = list[Human]


@dataclass
class DataProvider:
    _faker: Faker = field(default_factory=Faker)

    def _generate_group_names(
        self,
        amount: int = 10,
    ) -> T_GROUP_NAMES:
        return [self._faker.unique.company() for _ in range(amount)]

    def _generate_human(self, group_name: T_GROUP_NAME) -> Human:
        return Human(
            name=self._faker.unique.first_name(),
            group=group_name,
        )

    def _generate_humans(self, groups: T_GROUP_NAMES, amount_of_humans: int) -> T_HUMANS:
        members = []
        for _ in range(amount_of_humans):
            group_name = random.choice(groups)
            group_member = self._generate_human(group_name=group_name)
            members.append(group_member)

        return members

    def generate_group_members(
        self,
        amount_of_groups: None | int = None,
        amount_of_humans: None | int = None,
    ) -> T_HUMANS:
        amount_of_groups = amount_of_groups or random.randint(5, 10)
        amount_of_humans = amount_of_humans or random.randint(3, 30)

        _groups = self._generate_group_names(amount=amount_of_groups)
        return self._generate_humans(groups=_groups, amount_of_humans=amount_of_humans)


def organize_data(humans: T_HUMANS):
    # Will receive List of Dictionaries with single Name & single Company in each

    # Create a dictionary to store group information:
    group_info = {}

    # Iterate through the data and populate the group_info dictionary:
    for each in humans:
        group_name = each["group"]
        if group_name not in group_info:
            group_info[group_name] = {"users": 0, "names": []}
        group_info[group_name]["users"] += 1
        group_info[group_name]["names"].append(each["name"])

    return group_info


def get_formatted_output(data) -> str:
    # Print the group information:
    for group_name, info in data.items():
        print(f"Group: {group_name}")
        print(f"Number of Users: {info['users']}")
        print(f"Names: {', '.join(info['names'])}")
        print()


def main():
    """
    You have a list of humans. Every human have "name" and "group".
    Your task is to show all groups, with amount and names of members of each group.
    """
    # Creates Random amount of Companies-groups & random amount of ppl in it:
    group_members = DataProvider().generate_group_members()

    organized_data = organize_data(humans=group_members)

    get_formatted_output(data=organized_data)


if __name__ == "__main__":
    main()
