''''
    RULES FOR ALL CARDS CONSIDERING A MILITARY STRATEGY
'''


## ==========    WONDER IDS ==============================
# ( A, B) = GIZA(0, 7), BABYLON(1, 8), OLYMPIA(2, 9), RHODOS(3, 10), EPHESOS(4, 11), ALEXANDRIA(5, 12),
# HALIKARNASSOS(6, 13)
## ==================================================================

def find_card(player_state, card):
    size = len(player_state["cards_hand"])
    is_in_hand = False

    for i in range(size):
        if player_state["cards_hand"][i] == card:
            is_in_hand = True

    return is_in_hand


def count_cards_played_matchs(player_state, type):
    size = len(player_state["cards_played"])
    count = 0

    for i in range(size):
        for j in range(len(type)):
            if player_state["cards_played"][i] == type[j]:
                count += 1

    return count


def qt_civilian_structure(player_state):
    civilian_structure = ["Altar", "Theater", "Pawnshop", "Baths", "Temple", "Courthouse", "Statue", "Aqueduct",
                          "Gardens", "Town Hall", "Senate", "Pantheon", "Palace"]

    count_civilian_structure = count_cards_played_matchs(player_state, civilian_structure)

    return count_civilian_structure


def qt_commercial_structure(player_state):
    commercial_structure = ["Tavern", "East Trading Post", "West Trading Post", "Marketplace", "Forum", "Caravansery",
                            "Vineyard", "Bazar", "Haven", "Lighthouse", "Chamber of Commerce", "Arena"]

    count_commercial_structure = count_cards_played_matchs(player_state, commercial_structure)

    return count_commercial_structure


def qt_military_structure(player_state):
    military_structure = ["Stockade", "Barracks", "Guard Tower", "Walls", "Training Ground", "Stables",
                          "Archery Range", "Fortifications", "Circus", "Arsenal", "Siege Workshop"]

    count_military_structure = count_cards_played_matchs(player_state, military_structure)

    return count_military_structure


def qt_scientific_structure(player_state):
    scientific_structure = ["Apothecary", "Workshop", "Scriptorium", "Dispensary", "Laboratory", "Library",
                            "School", "Lodge", "Observatory", "University", "Academy", "Study"]

    count_scientific_structure = count_cards_played_matchs(player_state, scientific_structure)

    return count_scientific_structure


def qt_trading_post(player_state):
    east_trading_post_card = "East Trading Post"
    west_trading_post_card = "West Trading Post"
    count_trading_post = 0

    east_trading_post_card = find_card(player_state, east_trading_post_card)
    west_trading_post_card = find_card(player_state, west_trading_post_card)

    if east_trading_post_card:
        count_trading_post += 1
    if west_trading_post_card:
        count_trading_post += 1

    return count_trading_post


def qt_shields(player_state):
    military_structure = ["Stockade", "Barracks", "Guard Tower", "Walls", "Training Ground", "Stables",
                          "Archery Range", "Fortifications", "Circus", "Arsenal", "Siege Workshop"]

    size = len(player_state["cards_played"])
    count = 0

    for i in range(size):
        for j in range(len(military_structure)):
            if player_state["cards_played"][i] == military_structure[j]:
                if (j == 0) | (j == 1) | (j == 2):
                    count += 1
                elif (j == 3) | (j == 4) | (j == 5) | (j == 6):
                    count += 2
                else:
                    count += 3
    return count


def lumber_yard(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    # Wonder: ALEXANDRIA B(12) Is important to play 1 Wood card and unlock the first stage
    if player_state["wonder_id"] == 12:
        return 4

    # Wonder: GIZA B(7) unlock the 1st stage
    if player_state["wonder_id"] == 7:
        return 4

    # Wonder:  OLYMPIA A(2) build your 1st stage
    if player_state["wonder_id"] == 2:
        return 5

    # Monopoly of wood
    if amount_raw_material < 2:
        return 4

    return 1


def stone_pit(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    # Wonder: GIZA B(7) unlock the 2nd stage
    if player_state["wonder_id"] == 7:
        return 3

    # Wonder:  OLYMPIA A(2) build the 2nd stage
    if player_state["wonder_id"] == 2:
        return 4

    # Wonder: RHODOS B(10) neighbors logic
    # if gizah isn't present
    if neighbors[0]["wonder_id"] != 7 | neighbors[0]["wonder_id"] != 0 \
            | neighbors[1]["wonder_id"] != 7 | neighbors[1]["wonder_id"] != 0:
        return 1
    else:
        return 3

    if amount_raw_material < 2:
        return 3

    return 1


def clay_pool(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]
    clay = player_state["resources"]["clay"]

    # Wonder: ALEXANDRIA B(12) Is important to play 1 Clay card and unlock the first stage
    if player_state["wonder_id"] == 12:
        return 4

    # Wonder: BABYLON B(8)
    if player_state["wonder_id"] == 8:
        if clay < 2:
            return 3

    # Wonder: GIZA B(7) unlock the 3rd stage
    if player_state["wonder_id"] == 7:
        return 2

    # Wonder: HALIKARNASSOS B(13) unlock your 2nd stage
    if player_state["wonder_id"] == 13:
        return 4

    if amount_raw_material < 2:
        return 3

    return 1


def ore_vein(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    # Wonder: OLYMPIA A(2) build the 3rd stage
    if player_state["wonder_id"] == 2:
        return 3

    # Wonder: HALIKARNASSOS B(13) unlock your 1nd stage
    if player_state["wonder_id"] == 13:
        return 3

    if amount_raw_material < 2:
        return 3

    return 1


def three_farm(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    # Wonder: GIZA B(7) unlock 2 stages of your wonder
    if player_state["wonder_id"] == 7:
        return 5

    if amount_raw_material < 2:
        return 3

    return 1


def excavation(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    if amount_raw_material < 2:
        return 3

    return 1


def clay_pit(player_state, game_state, neighbors):
    clay = player_state["resources"]["clay"]

    # Wonder: BABYLON B(8)
    if player_state["wonder_id"] == 8:
        if clay < 2:
            return 3

    # Wonder: HALIKARNASSOS B(13) you need both resources to build your stages
    if player_state["wonder_id"] == 13:
        return 5

    # starts with Rhodes or Babylon ?
    if game_state["era"] > 1 | (player_state["wonder_id"] == 3 | player_state["wonder_id"] == 10 |
                                player_state["wonder_id"] == 1 | player_state["wonder_id"] == 8):
        return 3

    return 5


def timber_yard(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    # starts with Rhodes or Babylon ?
    if (player_state["wonder_id"] == 3 | player_state["wonder_id"] == 10 |
            player_state["wonder_id"] == 1 | player_state["wonder_id"] == 8):
        return 5

    if amount_raw_material < 3:
        return 3

    return 1


def forest_cave(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    if amount_raw_material < 2:
        return 3

    return 1


def mine(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    if amount_raw_material < 2:
        return 3

    return 1


def sawmill(player_state, game_state, neighbors):
    amount_wood = player_state["resources"]["wood"]

    # Wonder: EPHESOS B(11) monopoly of wood
    if player_state["wonder_id"] == 11:
        return 2

    # Wonder: ALEXANDRIA B(12) Is important to play 1 Clay card and unlock the first stage
    if player_state["wonder_id"] == 12:
        if amount_wood < 1:
            return 4
        else:
            return 2

    # Wonder: BABYLON B(8) your 2nd wonder needs and you can do the monopoly
    if player_state["wonder_id"] == 8:
        return 4

    # Wonder: GIZA B(7) unlock the 3rd stage
    if player_state["wonder_id"] == 7:
        if amount_wood < 1:
            return 5

    # Wonder:  OLYMPIA A(2)
    if amount_wood < 2 & (neighbors[0]["resources"]["wood"] == 0 | neighbors[1]["resources"]["wood"] == 0 |player_state["resources"]["coins"] == 0):
        return 3

    # Wonder: RHODOS B(10) neighbors logic
    # if gizah isn't present
    if neighbors[0]["wonder_id"] != 7 | neighbors[0]["wonder_id"] != 0 \
            | neighbors[1]["wonder_id"] != 7 | neighbors[1]["wonder_id"] != 0:
        return 5

    if amount_wood < 2:
        return 2

    return 1


def quarry(player_state, game_state, neighbors):
    amount_stone = player_state["resources"]["stone"]

    # Wonder: ALEXANDRIA B(12) Is important to play 1 Clay card and unlock the first stage
    if player_state["wonder_id"] == 12:
        return 4

    # Wonder: BABYLON B(8) allows to try to pick some cards like: Wall | Tablet | Compass
    if player_state["wonder_id"] == 8:
        return 3

    # Wonder: RHODOS B(10) allows to try to pick some cards like: Wall | Tablet | Compass
    if player_state["wonder_id"] == 8:
        return 5

    # Wonder: GIZA B(7) unlock the 3rd stage
    if player_state["wonder_id"] == 7:
        if amount_stone < 2:
            return 3
        elif amount_stone < 1:
            return 4

    # Wonder:  OLYMPIA A(2)
    if player_state["wonder_id"] == 2:
        if amount_stone < 2:
            return 4

    # Wonder: HALIKARNASSOS B(13) unlock your 1nd stage
    if player_state["wonder_id"] == 13:
        return 3

    # Pay attention to this card so you can build Wall
    return 2


def brickyard(player_state, game_state, neighbors):
    amount_clay = player_state["resources"]["clay"]

    # Wonder: EPHESOS B(11) gives you: Gear | Forum for free.
    if player_state["wonder_id"] == 11:
        return 3

    # Wonder: BABYLON B(8) allows to try to pick some cards like: Wall | Tablet | Compass
    if player_state["wonder_id"] == 8:
        if amount_clay < 2:
            return 3

    # Wonder: GIZA B(7) unlock the 3rd stage
    if player_state["wonder_id"] == 7:
        if amount_clay < 2:
            return 2
        elif amount_clay < 1:
            return 3

    # Wonder: HALIKARNASSOS B(13) unlock your 1nd stage
    if player_state["wonder_id"] == 13:
        if amount_clay < 2:
            return 4
        elif amount_clay < 1:
            return 5

    return 1


def foundry(player_state, game_state, neighbors):
    amount_ore = player_state["resources"]["ore"]

    # Wonder: EPHESOS B(11) links very well with: Compass | Theater | Hero guild.
    if player_state["wonder_id"] == 11:
        return 3

    # Wonder: RHODOS B(10) you need 4x ore to build your 2nd stage
    if player_state["wonder_id"] == 8:
        return 4

    # Wonder:  OLYMPIA A(2)
    if player_state["wonder_id"] == 2:
        if amount_ore < 2:
            return 4

    # Wonder: HALIKARNASSOS B(13)
    if player_state["wonder_id"] == 13:
        if amount_ore < 2:
            return 2
        elif amount_ore < 1:
            return 5

    return 1


def loom(player_state, game_state, neighbors):
    is_in_hand = find_card(player_state, "Marketplace")
    glass = player_state["resources"]["glass"]
    loom = player_state["resources"]["loom"]

    # Wonder: EPHESOS B(11)
    if player_state["wonder_id"] == 11:
        if loom < 1:
            return 4

    # Wonder: BABYLON B(8)
    if player_state["wonder_id"] == 8:
        if loom < 1:
            return 3

    # Wonder: RHODOS B(10)
    if player_state["wonder_id"] == 8:
        if loom < 1:
            return 3

    # Wonder:  OLYMPIA A(2) you can get the compass and get a free chain to the red card Stables
    if player_state["wonder_id"] == 2:
        if loom < 1:
            return 4

    if (not is_in_hand) & (glass < 1) & (loom < 1):
        return 4
    elif not is_in_hand:
        return 2

    return 1


def glassworks(player_state, game_state, neighbors):
    is_in_hand = find_card(player_state, "Marketplace")
    glass = player_state["resources"]["glass"]
    loom = player_state["resources"]["loom"]

    # Wonder: EPHESOS B(11)
    if player_state["wonder_id"] == 11:
        if glass < 1:
            return 4

    # Wonder: BABYLON B(8)
    if player_state["wonder_id"] == 8:
        if glass < 1:
            return 2

    # Wonder: RHODOS B(10)
    if player_state["wonder_id"] == 8:
        if glass < 1:
            return 3

    # Wonder: HALIKARNASSOS B(13) to build stage && play militar
    if player_state["wonder_id"] == 13:
        if glass < 1:
            return 5

    if (not is_in_hand) & (glass < 1) & (loom < 1):
        return 4

    if not is_in_hand:
        return 2

    return 1


def press(player_state, game_state, neighbors):
    papyrus = player_state["resources"]["papyrus"]

    # Wonder: BABYLON B(8)
    if player_state["wonder_id"] == 8:
        if papyrus < 1:
            return 3

    # Wonder: GIZA B(7) Apart from Paper, you can freely ignore the gray resources and get a lot of brown resources
    if player_state["wonder_id"] == 7:
        return 4

    # Wonder: HALIKARNASSOS B(13) build stage
    if player_state["wonder_id"] == 13:
        if papyrus < 1:
            return 4

    return 1


def altar(player_state, game_state, neighbors):
    return 1


def theater(player_state, game_state, neighbors):
    return 1


def pawnshop(player_state, game_state, neighbors):
    return 2


def baths(player_state, game_state, neighbors):
    return 2


def temple(player_state, game_state, neighbors):
    count_civilian_structure = qt_civilian_structure(player_state)

    if count_civilian_structure < 2:
        return 3

    return 1


def courthouse(player_state, game_state, neighbors):
    count_civilian_structure = qt_civilian_structure(player_state)

    if count_civilian_structure < 2:
        return 3

    return 1


def statue(player_state, game_state, neighbors):
    count_civilian_structure = qt_civilian_structure(player_state)

    if count_civilian_structure < 2:
        return 3

    return 1


def aqueduct(player_state, game_state, neighbors):
    count_civilian_structure = qt_civilian_structure(player_state)

    if count_civilian_structure < 2:
        return 3

    return 1


def gardens(player_state, game_state, neighbors):
    return 3


def town_hall(player_state, game_state, neighbors):
    return 4


def senate(player_state, game_state, neighbors):
    return 4


def pantheon(player_state, game_state, neighbors):
    return 5


def palace(player_state, game_state, neighbors):
    return 5


def tavern(player_state, game_state, neighbors):
    return 1


def east_trading_post(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]
    amount_raw_material_right_neighbor = neighbors[1]["resources"]["clay"] + neighbors[1]["resources"]["ore"] + \
                                         neighbors[1]["resources"]["wood"] + neighbors[1]["resources"]["stone"]

    amount_raw_material_left_neighbor = neighbors[0]["resources"]["clay"] + neighbors[0]["resources"]["ore"] + \
                                        neighbors[0]["resources"]["wood"] + neighbors[0]["resources"]["stone"]

    west_trading_post_card = "West Trading Post"
    marketplace_card = "Marketplace"

    west_trading_post_card = find_card(player_state, west_trading_post_card)
    marketplace_card = find_card(player_state, marketplace_card)

    count_trading_post = qt_trading_post(player_state)

    # if you cannot have the brown resources && your neighbor have
    if (amount_raw_material <= 1) & \
            (amount_raw_material_right_neighbor > 1 | amount_raw_material_left_neighbor > 1):
        return 4

    # Wonder: EPHESOS B(11) regular supply of money
    if player_state["wonder_id"] == 11:
        return 3

    # Wonder: ALEXANDRIA B(12)
    if player_state["wonder_id"] == 12:
        if west_trading_post_card & marketplace_card:
            return 1
        elif west_trading_post_card | marketplace_card:
            return 4
        else:
            return 4

    # Wonder: GIZA B(7)
    if player_state["wonder_id"] == 7:
        if count_trading_post < 1:
            return 4

    # Wonder:  OLYMPIA A(2) Trading Post continues a good card for military because you need a lot of brown resources
    if player_state["wonder_id"] == 2:
        return 4

    # Wonder: HALIKARNASSOS B(13) Pick the Trading Post is never a bad move
    if player_state["wonder_id"] == 13:
        return 4

    return 1


def west_trading_post(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]
    amount_raw_material_right_neighbor = neighbors[1]["resources"]["clay"] + neighbors[1]["resources"]["ore"] + \
                                         neighbors[1]["resources"]["wood"] + neighbors[1]["resources"]["stone"]

    amount_raw_material_left_neighbor = neighbors[0]["resources"]["clay"] + neighbors[0]["resources"]["ore"] + \
                                        neighbors[0]["resources"]["wood"] + neighbors[0]["resources"]["stone"]
    east_trading_post_card = "East Trading Post"
    marketplace_card = "Marketplace"

    east_trading_post_card = find_card(player_state, east_trading_post_card)
    marketplace_card = find_card(player_state, marketplace_card)

    count_trading_post = qt_trading_post(player_state)

    # if you cannot have the brown resources && your neighbor have
    if (amount_raw_material <= 1) & (amount_raw_material_right_neighbor > 1 | amount_raw_material_left_neighbor > 1):
        return 4

    # Wonder: EPHESOS B(11) regular supply of money
    if player_state["wonder_id"] == 11:
        return 3

    # Wonder: ALEXANDRIA B(12)
    if player_state["wonder_id"] == 12:
        if east_trading_post_card & marketplace_card:
            return 1
        elif east_trading_post_card | marketplace_card:
            return 4
        else:
            return 4

    # Wonder: GIZA B(7)
    if player_state["wonder_id"] == 7:
        if count_trading_post < 1:
            return 4

    # Wonder:  OLYMPIA A(2) Trading Post continues a good card for military because you need a lot of brown resources
    if player_state["wonder_id"] == 2:
        return 4

    # Wonder: HALIKARNASSOS B(13) Pick the Trading Post is never a bad move
    if player_state["wonder_id"] == 13:
        return 4

    return 1


def marketplace(player_state, game_state, neighbors):
    east_trading_post_card = "East Trading Post"
    west_trading_post_card = "West Trading Post"

    east_trading_post_card = find_card(player_state, east_trading_post_card)
    west_trading_post_card = find_card(player_state, west_trading_post_card)

    # Wonder: ALEXANDRIA B(12)
    if player_state["wonder_id"] == 12:
        if east_trading_post_card & west_trading_post_card:
            return 1
        elif east_trading_post_card | west_trading_post_card:
            return 4
        else:
            return 4

    return 4


def forum(player_state, game_state, neighbors):
    is_in_hand = find_card(player_state, "Marketplace")
    glass = player_state["resources"]["glass"]
    loom = player_state["resources"]["loom"]
    amount_clay = player_state["resources"]["clay"]

    count_trading_post = qt_trading_post(player_state)

    # Wonder: EPHESOS B(11)
    if player_state["wonder_id"] == 11:
        if count_trading_post > 0 | amount_clay >= 2:
            return 5
        else:
            return 2

    # Wonder: GIZA B(7)
    if player_state["wonder_id"] == 7:
        if count_trading_post > 0:
            return 5

    if (not is_in_hand) & (glass < 1) & (loom < 1):
        return 4

    if not is_in_hand:
        return 2

    return 1


def caravansery(player_state, game_state, neighbors):
    return 5


def vineyard(player_state, game_state, neighbors):
    east_trading_post_card = "East Trading Post"
    west_trading_post_card = "West Trading Post"

    east_trading_post_card = find_card(player_state, east_trading_post_card)
    west_trading_post_card = find_card(player_state, west_trading_post_card)

    amount_raw_material_right_neighbor = neighbors[1]["resources"]["clay"] + neighbors[1]["resources"]["ore"] + \
                                         neighbors[1]["resources"]["wood"] + neighbors[1]["resources"]["stone"]

    amount_raw_material_left_neighbor = neighbors[0]["resources"]["clay"] + neighbors[0]["resources"]["ore"] + \
                                        neighbors[0]["resources"]["wood"] + neighbors[0]["resources"]["stone"]

    # Trading Post = 1 && neighboor have a lot of raw_material
    if (east_trading_post_card | west_trading_post_card) & \
            (amount_raw_material_right_neighbor >= 4 | amount_raw_material_left_neighbor >= 4):
        return 3

    return 1


def bazar(player_state, game_state, neighbors):
    amount_manufacture_good = player_state["resources"]["papyrus"] + player_state["resources"]["loom"] + \
                              player_state["resources"]["glass"]
    amount_raw_material_right_neighbor = neighbors[1]["resources"]["papyrus"] + neighbors[1]["resources"]["loom"] + \
                                         neighbors[1]["resources"]["glass"]
    amount_raw_material_left_neighbor = neighbors[0]["resources"]["papyrus"] + neighbors[0]["resources"]["loom"] + \
                                        neighbors[0]["resources"]["glass"]

    total_raw_material = amount_manufacture_good + amount_raw_material_right_neighbor + amount_raw_material_left_neighbor

    if total_raw_material >= 4:
        return 3

    return 1


def haven(player_state, game_state, neighbors):
    amount_raw_material = player_state["resources"]["clay"] + player_state["resources"]["ore"] \
                          + player_state["resources"]["wood"] + player_state["resources"]["stone"]

    # Wonder: GIZA B(7) Just be sure you can pay for Textile to play the Haven
    if player_state["wonder_id"] == 7:
        return 4

    if amount_raw_material >= 4:
        return 3

    return 1


def lighthouse(player_state, game_state, neighbors):
    amount_of_commercial_structure = qt_commercial_structure(player_state)

    if amount_of_commercial_structure >= 4:
        return 3

    return 1


def chamber_of_commerce(player_state, game_state, neighbors):
    amount_manufacture_good = player_state["resources"]["papyrus"] + player_state["resources"]["loom"] \
                              + player_state["resources"]["glass"]

    if amount_manufacture_good >= 2:
        return 3

    return 1


def arena(player_state, game_state, neighbors):
    coins = player_state["resources"]["papyrus"]
    wonder_stage = player_state["wonder_stage"]

    if (coins < 3) & (wonder_stage >= 1):
        return 3

    return 1


def stockade(player_state, game_state, neighbors):
    amount_of_military_cards = qt_military_structure(player_state)

    if amount_of_military_cards < 2:
        return 4
    if amount_of_military_cards < 1:
        return 5

    return 1


def barracks(player_state, game_state, neighbors):
    amount_of_military_cards = qt_military_structure(player_state)

    if amount_of_military_cards < 2:
        return 4
    if amount_of_military_cards < 1:
        return 5

    return 1


def guard_tower(player_state, game_state, neighbors):
    amount_of_military_cards = qt_military_structure(player_state)

    if amount_of_military_cards < 2:
        return 4
    if amount_of_military_cards < 1:
        return 5

    return 1


def walls(player_state, game_state, neighbors):
    amount_of_military_cards = qt_shields(player_state)
    amount_military_cards_right_neighbor = qt_shields(neighbors[1])
    amount_military_cards_left_neighbor = qt_shields(neighbors[0])

    # military_structure < 1 || if you aren't the military leader
    if (amount_of_military_cards < 1) | (amount_military_cards_left_neighbor >= amount_of_military_cards) \
            | (amount_military_cards_right_neighbor >= amount_of_military_cards):
        return 5

    return 1


def training_ground(player_state, game_state, neighbors):
    amount_of_military_cards = qt_shields(player_state)
    amount_military_cards_right_neighbor = qt_shields(neighbors[1])
    amount_military_cards_left_neighbor = qt_shields(neighbors[0])

    # military_structure < 1 || if you aren't the military leader
    if (amount_of_military_cards < 1) | (amount_military_cards_left_neighbor >= amount_of_military_cards) \
            | (amount_military_cards_right_neighbor >= amount_of_military_cards):
        return 5

    return 1


def stables(player_state, game_state, neighbors):
    amount_of_military_cards = qt_shields(player_state)
    amount_military_cards_right_neighbor = qt_shields(neighbors[1])
    amount_military_cards_left_neighbor = qt_shields(neighbors[0])

    # military_structure < 1 || if you aren't the military leader
    if (amount_of_military_cards < 1) | (amount_military_cards_left_neighbor >= amount_of_military_cards) \
            | (amount_military_cards_right_neighbor >= amount_of_military_cards):
        return 5

    return 1


def archery_range(player_state, game_state, neighbors):
    amount_of_military_cards = qt_shields(player_state)
    amount_military_cards_right_neighbor = qt_shields(neighbors[1])
    amount_military_cards_left_neighbor = qt_shields(neighbors[0])

    # military_structure < 1 || if you aren't the military leader
    if (amount_of_military_cards < 1) | (amount_military_cards_left_neighbor >= amount_of_military_cards) \
            | (amount_military_cards_right_neighbor >= amount_of_military_cards):
        return 5

    return 1


def fortifications(player_state, game_state, neighbors):
    amount_of_military_cards = qt_shields(player_state)
    amount_military_cards_right_neighbor = qt_shields(neighbors[1])
    amount_military_cards_left_neighbor = qt_shields(neighbors[0])
    my_amount_plus_this_card = amount_of_military_cards + 3

    # you need this card for win?
    if (amount_of_military_cards < 1) | (amount_military_cards_left_neighbor >= amount_of_military_cards) \
            | (amount_military_cards_right_neighbor >= amount_of_military_cards):
        if(my_amount_plus_this_card >= amount_military_cards_left_neighbor) | (my_amount_plus_this_card >= amount_military_cards_right_neighbor):
            return 5

    return 1


def circus(player_state, game_state, neighbors):
    amount_of_military_cards = qt_shields(player_state)
    amount_military_cards_right_neighbor = qt_shields(neighbors[1])
    amount_military_cards_left_neighbor = qt_shields(neighbors[0])
    my_amount_plus_this_card = amount_of_military_cards + 3

    # you need this card for win?
    if (amount_of_military_cards < 1) | (amount_military_cards_left_neighbor >= amount_of_military_cards) \
            | (amount_military_cards_right_neighbor >= amount_of_military_cards):
        if(my_amount_plus_this_card >= amount_military_cards_left_neighbor) | (my_amount_plus_this_card >= amount_military_cards_right_neighbor):
            return 5

    return 1


def arsenal(player_state, game_state, neighbors):
    amount_of_military_cards = qt_shields(player_state)
    amount_military_cards_right_neighbor = qt_shields(neighbors[1])
    amount_military_cards_left_neighbor = qt_shields(neighbors[0])
    my_amount_plus_this_card = amount_of_military_cards + 3

    # you need this card for win?
    if (amount_of_military_cards < 1) | (amount_military_cards_left_neighbor >= amount_of_military_cards) \
            | (amount_military_cards_right_neighbor >= amount_of_military_cards):
        if(my_amount_plus_this_card >= amount_military_cards_left_neighbor) | (my_amount_plus_this_card >= amount_military_cards_right_neighbor):
            return 5

    return 1


def siege_workshop(player_state, game_state, neighbors):
    amount_of_military_cards = qt_shields(player_state)
    amount_military_cards_right_neighbor = qt_shields(neighbors[1])
    amount_military_cards_left_neighbor = qt_shields(neighbors[0])
    my_amount_plus_this_card = amount_of_military_cards + 3

    # you need this card for win?
    if (amount_of_military_cards < 1) | (amount_military_cards_left_neighbor >= amount_of_military_cards) \
            | (amount_military_cards_right_neighbor >= amount_of_military_cards):
        if(my_amount_plus_this_card >= amount_military_cards_left_neighbor) | (my_amount_plus_this_card >= amount_military_cards_right_neighbor):
            return 5

    return 1


def apothecary(player_state, game_state, neighbors):
    return 1


def workshop(player_state, game_state, neighbors):
    # Wonder: EPHESOS B(11)
    if player_state["wonder_id"] == 11:
        return 2

    return 1


def scriptorium(player_state, game_state, neighbors):
    # Wonder: EPHESOS B(11) free Tablet
    if player_state["wonder_id"] == 11:
        return 5

    return 1


def dispensary(player_state, game_state, neighbors):
    amount_ore = player_state["resources"]["ore"]
    amount_glass = player_state["resources"]["glass"]
    amount_scientific_structure = qt_scientific_structure(player_state)

    # Wonder: EPHESOS B(11) free Tablet
    if player_state["wonder_id"] == 11:
        if (amount_ore >= 2) & amount_glass & (amount_scientific_structure < 3):
            return 2

    return 1


def laboratory(player_state, game_state, neighbors):
    amount_ore = player_state["resources"]["ore"]
    amount_scientific_structure = qt_scientific_structure(player_state)

    # Wonder: EPHESOS B(11) free Tablet
    if player_state["wonder_id"] == 11:
        if (amount_ore >= 2) & (amount_scientific_structure < 3):
            return 3
        else:
            return 2

    return 1


def library(player_state, game_state, neighbors):
    amount_stone = player_state["resources"]["stone"]

    # Wonder: HALIKARNASSOS B(13)
    if player_state["wonder_id"] == 13:
        if amount_stone >= 2:
            return 5

    return 1


def school(player_state, game_state, neighbors):
    amount_scientific_structure = qt_scientific_structure(player_state)

    # Wonder: EPHESOS B(11) free Tablet
    if player_state["wonder_id"] == 11:
        if amount_scientific_structure < 2:
            return 2

    return 1


def lodge(player_state, game_state, neighbors):
    return 1


def observatory(player_state, game_state, neighbors):
    return 1


def university(player_state, game_state, neighbors):
    return 1


def academy(player_state, game_state, neighbors):
    return 1


def study(player_state, game_state, neighbors):
    return 1


def workers_guild(player_state, game_state, neighbors):
    return 1


def craftsmens_guild(player_state, game_state, neighbors):
    return 1


def traders_guild(player_state, game_state, neighbors):
    return 1


def philosophers_guild(player_state, game_state, neighbors):
    return 1


def spies_guild(player_state, game_state, neighbors):
    return 1


def magistrates_guild(player_state, game_state, neighbors):
    return 1


def shipowners_guild(player_state, game_state, neighbors):
    return 1


def strategists_guild(player_state, game_state, neighbors):
    # Wonder: RHODOS B(10) allows to try to pick some cards like: Wall | Tablet | Compass
    if player_state["wonder_id"] == 8:
        return 5
    return 1


def scientists_guild(player_state, game_state, neighbors):
    coins = player_state["resources"]["coins"]

    # Wonder: EPHESOS B(11) free Tablet
    if player_state["wonder_id"] == 11:
        if coins >= 2:
            return 4

    return 1


def builders_guild(player_state, game_state, neighbors):
    return 1


# map of functions applied for a specific card
card_weight_map = {
    '1': lumber_yard,
    '2': stone_pit,
    '3': clay_pool,
    '4': ore_vein,
    '5': three_farm,
    '6': excavation,
    '7': clay_pit,
    '8': timber_yard,
    '9': forest_cave,
    '10': mine,
    '11': sawmill,
    '12': quarry,
    '13': brickyard,
    '14': foundry,
    '15': loom,
    '16': glassworks,
    '17': press,
    '18': altar,
    '19': theater,
    '20': pawnshop,
    '21': baths,
    '22': temple,
    '23': courthouse,
    '24': statue,
    '25': aqueduct,
    '26': gardens,
    '27': town_hall,
    '28': senate,
    '29': pantheon,
    '30': palace,
    '31': tavern,
    '32': east_trading_post,
    '33': west_trading_post,
    '34': marketplace,
    '35': forum,
    '36': caravansery,
    '37': vineyard,
    '38': bazar,
    '39': haven,
    '40': lighthouse,
    '41': chamber_of_commerce,
    '42': arena,
    '43': stockade,
    '44': barracks,
    '45': guard_tower,
    '46': walls,
    '47': training_ground,
    '48': stables,
    '49': archery_range,
    '50': fortifications,
    '51': circus,
    '52': arsenal,
    '53': siege_workshop,
    '54': apothecary,
    '55': workshop,
    '56': scriptorium,
    '57': dispensary,
    '58': laboratory,
    '59': library,
    '60': school,
    '61': lodge,
    '62': observatory,
    '63': university,
    '64': academy,
    '65': study,
    '66': workers_guild,
    '67': craftsmens_guild,
    '68': traders_guild,
    '69': philosophers_guild,
    '70': spies_guild,
    '71': magistrates_guild,
    '72': shipowners_guild,
    '73': strategists_guild,
    '74': scientists_guild,
    '75': builders_guild,
}
