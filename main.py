candidates = {"green": 0,
              "yellow": 0,
              "blue": 0,
              "white": 0,
              "red": 0}


def election():
    round2 = True
    total = 0
    for each in candidates:
        score = int(input("how many votes did " + each + " obtained ? :"))
        candidates[each] = score
        total += score

    candidate_percentages = {"green": (candidates["green"] / total) * 100,
                             "yellow": (candidates["yellow"] / total) * 100,
                             "blue": (candidates["blue"] / total) * 100,
                             "white": (candidates["white"] / total) * 100,
                             "red": (candidates["red"] / total) * 100}

    for each in candidate_percentages:
        print(str(each) + "......." + str(round(candidate_percentages[each], 2)) + "%")

    if candidate_percentages["yellow"] > 50:
        print("candidate yellow is elected in the first round")
        round2 = False
    elif candidate_percentages["yellow"] < 50:
        for each in candidate_percentages:
            if candidate_percentages[each] > 50:
                round2 = False
                print("yellow lost in the first round")
                break
    if round2:
        if 12.5 <= candidate_percentages["yellow"] <= 50 \
                and max(candidate_percentages, key=candidate_percentages.get) == "yellow":
            print("candidate yellow is admitted in the second round, in a strong position")
        elif 12.5 <= candidate_percentages["yellow"] <= 50 \
                and max(candidate_percentages, key=candidate_percentages.get) != "yellow":
            print("candidate yellow is admitted in the second round, in a weak position")
        elif 12.5 > candidate_percentages["yellow"]:
            print("candidate yellow is not admitted in the second round")


election()
