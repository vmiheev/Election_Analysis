counties = ["Arapahoe", "Denver", "Jefferson"]

# for county in counties:
#     print(county)

# for i in range(len(counties)):
#     print(counties[i])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict.keys():
#     print(county)
#     print(counties_dict[county])

# for voters in counties_dict.values():
#     print(voters)

# for county, voters in counties_dict.items():
#     print(county,"county has",voters,"registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    # for value in county_dict.values():
    #     print(value)
    print(county_dict["registered_voters"])