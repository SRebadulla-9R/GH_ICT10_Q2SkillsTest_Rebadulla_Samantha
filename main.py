# skills test !!

# Dictionary 
school_clubs = {
    "Science Club": [
        "Explore scientific experiments and projects.",
        "Fridays, 3:00 PM",
        "Room 101",
        "Mr. Santos",
        25
    ],
    "Art Club": [
        "Express creativity through painting, sculpture, and crafts.",
        "Wednesdays, 2:30 PM",
        "Art Studio",
        "Ms. Reyes",
        30
    ],
    "Math Club": [
        "Solve challenging math problems and participate in competitions.",
        "Mondays, 3:30 PM",
        "Room 202",
        "Mr. Cruz",
        20
    ],
    "Drama Club": [
        "Perform plays and learn acting techniques.",
        "Thursdays, 4:00 PM",
        "Auditorium",
        "Ms. Gomez",
        18
    ],
    "Music Club": [
        "Learn and perform musical pieces.",
        "Tuesdays, 3:00 PM",
        "Music Room",
        "Mr. De Leon",
        22
    ],
    "Debate Club": [
        "Develop public speaking and argumentation skills.",
        "Fridays, 2:00 PM",
        "Room 305",
        "Ms. Tan",
        28
    ],
    "Environmental Club": [
        "Participate in eco-friendly projects and campaigns.",
        "Thursdays, 3:30 PM",
        "Room 110",
        "Ms. Flores",
        24
    ],
    "Volleyball Varsity": [
        "Represent the school in volleyball competitions.",
        "Mondays & Wednesdays, 5:00 PM",
        "Gymnasium",
        "Coach Rivera",
        15
    ],
    "Basketball Varsity": [
        "Compete in basketball tournaments and training.",
        "Tuesdays & Thursdays, 5:00 PM",
        "Gymnasium",
        "Coach Morales",
        16
    ],
    "Baking Club": [
        "Learn baking techniques and share recipes.",
        "Fridays, 2:30 PM",
        "Home Economics Room",
        "Ms. Delos Santos",
        20
    ]
}

# display club info (taken from youtube..)
def display_club_info(club_name):
    keys = ["Description", "Meeting Time", "Location", "Club Moderator", "Number of Members"]
    values = school_clubs.get(club_name, ["N/A"] * 5)
    print(f"===== {club_name} =====")
    for k, v in zip(keys, values):
        print(f"{k}: {v}")
    print("\n")

# Display club
for club in school_clubs:
    display_club_info(club)
