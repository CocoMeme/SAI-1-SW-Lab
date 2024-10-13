def professors_subjects(**kwargs):
    for prof, subject in kwargs.items():
        print(f"{prof}: {subject}")

professors_subjects(Valdez="System Architecture Management", 
                    Madriaga="Information Assurance", 
                    Dalisay="React JS", 
                    Lappay="Bootstrap")
