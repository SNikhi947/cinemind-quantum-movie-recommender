import json
import os

def generate_large_dataset():
    # Helper to generate movie dict
    def m(id, title, genres, lang, keywords, poster_keyword):
        # We construct a descriptive overview so the ML has words to match against user prompts
        overview = f"A {lang} {genres[0]} movie titled {title}. Key themes include {keywords}. Highly rated and popular in {lang} cinema."
        return {
            "id": id,
            "title": title,
            "genres": genres,
            "language": lang,
            "overview": overview,
            # Using a dynamic image service that puts the text on the image so you know it works
            "poster_url": f"https://placehold.co/300x450/111/fff?text={title.replace(' ', '+')}",
            "trailer_url": f"https://www.youtube.com/results?search_query={title.replace(' ', '+')}+trailer",
            "rating": 9.0
        }

    movies = []
    idx = 1

    # --- TELUGU (Tollywood) ---
    telugu_hits = [
        ("Kalki 2898 AD", ["Sci-Fi", "Action"], "dystopian future, mythology, vishnu avatar, war"),
        ("RRR", ["Action", "Drama"], "friendship, british raj, revolution, fire and water"),
        ("Baahubali: The Beginning", ["Action", "Fantasy"], "kingdom, war, betrayal, destiny"),
        ("Baahubali 2: The Conclusion", ["Action", "Fantasy"], "revenge, kingdom, mother sentiment, epic war"),
        ("Salaar: Part 1", ["Action", "Crime"], "gangster, friendship, khansaar, violence"),
        ("Pushpa: The Rise", ["Action", "Drama"], "red sandalwood smuggling, attitude, rise to power"),
        ("Pushpa 2: The Rule", ["Action", "Crime"], "syndicate rule, police conflict, revenge"),
        ("Rangasthalam", ["Action", "Drama"], "village politics, hearing impaired, revenge, brother sentiment"),
        ("Arjun Reddy", ["Romance", "Drama"], "anger management, doctor, heartbreak, self-destruction"),
        ("Jersey", ["Drama", "Sports"], "cricket, father son bond, late success, comeback"),
        ("Mahanati", ["Biography", "Drama"], "actress savitri life, rise and fall, emotional"),
        ("Eega", ["Fantasy", "Comedy"], "housefly revenge, reincarnation, love story, villain"),
        ("Ala Vaikunthapurramuloo", ["Comedy", "Action"], "middle class vs rich, swapped babies, style"),
        ("Magadheera", ["Action", "Fantasy"], "reincarnation, 400 years ago, warrior, love"),
        ("Pokiri", ["Action", "Thriller"], "undercover cop, mafia, gangster, twist"),
        ("Kick", ["Action", "Comedy"], "adrenaline junkie, thief, police chase, fun"),
        ("Race Gurram", ["Action", "Comedy"], "brother rivalry, police, politician villain, fun"),
        ("Manam", ["Drama", "Fantasy"], "reincarnation, 3 generations, family love, magical"),
        ("Ye Maaya Chesave", ["Romance", "Drama"], "classic love story, religion conflict, chemistry"),
        ("Leader", ["Drama", "Political"], "cm son, corruption, political reform, journey"),
        ("Vedam", ["Drama", "Anthology"], "5 stories, terrorist attack, hospital, humanity"),
        ("C/o Kancharapalem", ["Drama", "Romance"], "anthology, village life, pure love, slice of life"),
        ("Goodachari", ["Thriller", "Action"], "spy, raw agent, father sentiment, twist"),
        ("Agent Sai Srinivasa Athreya", ["Thriller", "Comedy"], "detective, dead bodies mystery, fbi, humor"),
        ("Karthikeya 2", ["Adventure", "Fantasy"], "lord krishna, mystery, dwarka, treasure hunt"),
        ("Hanu-Man", ["Action", "Fantasy"], "superhero, lord hanuman, village savior, powers"),
        ("Baby", ["Romance", "Drama"], "first love, betrayal, college, emotional pain"),
        ("Hi Nanna", ["Drama", "Romance"], "single father, daughter, memory loss, emotional"),
        ("Sita Ramam", ["Romance", "Drama"], "letter, soldier, princess, war, poetic love"),
        ("Dasara", ["Action", "Drama"], "coal mines, friendship, village politics, raw"),
        ("Virupaksha", ["Horror", "Thriller"], "black magic, village mystery, occult, suspense"),
        ("Waltair Veerayya", ["Action", "Comedy"], "fisherman, brother sentiment, smuggler, fun"),
        ("Veera Simha Reddy", ["Action", "Drama"], "faction, sister sentiment, revenge, mass"),
        ("Guntur Kaaram", ["Action", "Drama"], "mother sentiment, trivikram style, mahesh babu"),
        ("Devara", ["Action", "Drama"], "sea, fear, corruption, ntr"),
        ("Game Changer", ["Political", "Action"], "election, corruption, shankar style, ram charan"),
        ("Og", ["Action", "Crime"], "gangster, mumbai, samurai, pawan kalyan"),
        ("Business Man", ["Crime", "Action"], "mumbai mafia, absolute power, surya bhai"),
        ("Khaleja", ["Action", "Comedy"], "god, taxi driver, village savior, philosophy"),
        ("Athadu", ["Action", "Thriller"], "assassin, family drama, hiding, village"),
    ]

    for t, g, k in telugu_hits:
        movies.append(m(idx, t, g, "Telugu", k, t))
        idx += 1

    # --- TAMIL (Kollywood) ---
    tamil_hits = [
        ("Leo", ["Action", "Thriller"], "LCU, gangster, hidden identity, hyena"),
        ("Vikram", ["Action", "Thriller"], "LCU, drugs, black squad, ghost"),
        ("Jailer", ["Action", "Comedy"], "retired cop, idol smuggling, family protection, mass"),
        ("Kaithi", ["Action", "Thriller"], "LCU, prisoner, night duty, biryani, drugs"),
        ("Master", ["Action", "Drama"], "professor, alcohol, juvenile home, jd vs bhavani"),
        ("Thuppakki", ["Action", "Thriller"], "sleeper cells, army man, mumbai, mind game"),
        ("Kaththi", ["Action", "Drama"], "farmers issue, corporate villain, double role, water"),
        ("Mersal", ["Action", "Drama"], "medical mafia, magician, doctor, three roles"),
        ("Bigil", ["Sports", "Action"], "women football, gangster father, coach, motivation"),
        ("96", ["Romance", "Drama"], "school love, reunion, memories, night journey"),
        ("Asuran", ["Action", "Drama"], "caste oppression, land rights, father revenge, violent"),
        ("Vada Chennai", ["Crime", "Drama"], "north chennai, carrom player, gangster wars, prison"),
        ("Ratsasan", ["Thriller", "Crime"], "psycho killer, school girls, police, dark"),
        ("Soorarai Pottru", ["Drama", "Biography"], "flight cost, airline business, struggle, dream"),
        ("Jai Bhim", ["Drama", "Legal"], "tribal justice, lawyer, police brutality, court"),
        ("Super Deluxe", ["Drama", "Thriller"], "hyperlink story, transgender, aliens, infidelity"),
        ("Ponniyin Selvan 1", ["History", "Drama"], "chola dynasty, throne war, spies, epic"),
        ("Ponniyin Selvan 2", ["History", "Drama"], "love story, revenge, war, conclusion"),
        ("Mankatha", ["Action", "Crime"], "heist, betting, dirty cop, money, vinayak mahadev"),
        ("Baasha", ["Action", "Crime"], "auto driver, don flashback, mumbai, brother sentiment"),
        ("Nayakan", ["Crime", "Drama"], "slum lord, mumbai don, justice, classic"),
        ("Anniyan", ["Thriller", "Action"], "multiple personality disorder, garuda puranam, corruption"),
        ("Sivaji: The Boss", ["Action", "Drama"], "black money, education, rich vs poor, style"),
        ("Enthiran", ["Sci-Fi", "Action"], "robot, chitti, love, destruction, ai"),
        ("2.0", ["Sci-Fi", "Action"], "cell phone radiation, bird man, robot return"),
        ("Thiruchitrambalam", ["Romance", "Comedy"], "delivery boy, best friend, simple life, family"),
        ("Love Today", ["Comedy", "Romance"], "phone exchange, secrets, modern relationship, funny"),
        ("Doctor", ["Comedy", "Thriller"], "human trafficking, deadpan humor, family rescue"),
        ("Don", ["Comedy", "Drama"], "college life, father sentiment, engineering, fun"),
        ("Maanaadu", ["Sci-Fi", "Thriller"], "time loop, political assassination, repeat"),
    ]

    for t, g, k in tamil_hits:
        movies.append(m(idx, t, g, "Tamil", k, t))
        idx += 1

    # --- HINDI (Bollywood) ---
    hindi_hits = [
        ("Jawan", ["Action", "Thriller"], "women army, farmer issue, healthcare, double role"),
        ("Pathaan", ["Action", "Thriller"], "spy universe, virus, patriot, soldier"),
        ("Animal", ["Action", "Drama"], "toxic relationship, father son, violence, revenge"),
        ("Dangal", ["Biography", "Sports"], "wrestling, father daughters, gold medal, patriotism"),
        ("PK", ["Comedy", "Drama"], "alien, religion, god men, funny question"),
        ("3 Idiots", ["Comedy", "Drama"], "engineering, education system, friends, all is well"),
        ("Sholay", ["Action", "Adventure"], "gabbar singh, friendship, bandits, revenge"),
        ("Dilwale Dulhania Le Jayenge", ["Romance", "Drama"], "euro trip, punjab, father approval, train"),
        ("Kabhi Khushi Kabhie Gham", ["Drama", "Romance"], "family values, rich poor gap, reunion, ego"),
        ("Yeh Jawaani Hai Deewani", ["Romance", "Drama"], "trekking, travel, career vs love, wedding"),
        ("Zindagi Na Milegi Dobara", ["Drama", "Adventure"], "bachelor trip, spain, fear, friendship"),
        ("Queen", ["Comedy", "Drama"], "honeymoon alone, paris, self discovery, independence"),
        ("Gangs of Wasseypur", ["Crime", "Action"], "coal mafia, revenge, generations, raw"),
        ("Stree", ["Horror", "Comedy"], "witch, respect women, village mystery, funny"),
        ("Bhool Bhulaiyaa", ["Horror", "Comedy"], "ghost dancer, psychological, palace, avni"),
        ("Drishyam", ["Thriller", "Crime"], "visual memory, police investigation, family protection"),
        ("Andhadhun", ["Thriller", "Comedy"], "blind pianist, murder witness, twist, pune"),
        ("Tumbbad", ["Horror", "Fantasy"], "greed, gold, goddess, curse, rain"),
        ("Lagaan", ["Sports", "Drama"], "british raj, cricket match, tax, village unity"),
        ("Swades", ["Drama", "Social"], "nasa scientist, india village, electricity, roots"),
        ("Bajrangi Bhaijaan", ["Drama", "Action"], "pakistan girl, hanuman devotee, border crossing"),
        ("Sultan", ["Sports", "Drama"], "wrestling, ego, comeback, love story"),
        ("War", ["Action", "Thriller"], "spy, teacher student, plastic surgery, twist"),
        ("Tiger 3", ["Action", "Thriller"], "spy universe, pakistan, family protection"),
        ("Brahmastra", ["Fantasy", "Action"], "astraverse, fire, love, ancient power"),
        ("12th Fail", ["Biography", "Drama"], "upsc exam, poverty, restart, inspiration"),
        ("Article 370", ["Drama", "Political"], "kashmir, terrorism, constitution, action"),
        ("Fighter", ["Action", "War"], "air force, pakistan, airstrike, patriotism"),
        ("Don 2", ["Action", "Thriller"], "asia underworld, berlin, heist, srk"),
        ("Rockstar", ["Drama", "Music"], "pain, fame, love, music journey"),
    ]

    for t, g, k in hindi_hits:
        movies.append(m(idx, t, g, "Hindi", k, t))
        idx += 1

    # --- MALAYALAM (Mollywood) ---
    malayalam_hits = [
        ("Manjummel Boys", ["Survival", "Thriller"], "guna cave, friendship, rescue, kodaikanal"),
        ("Premalu", ["Romance", "Comedy"], "hyderabad, software engineers, crush, funny"),
        ("Bramayugam", ["Horror", "Thriller"], "black and white, mansion, goblin, madness"),
        ("Aavesham", ["Action", "Comedy"], "bangalore, college ragging, gangster, ranga"),
        ("2018", ["Thriller", "Drama"], "floods, kerala, rescue, humanity, real story"),
        ("Lucifer", ["Action", "Political"], "stephen nedumpally, illuminati, politics, mass"),
        ("Drishyam", ["Thriller", "Crime"], "georgekutty, police station under construction, secret"),
        ("Drishyam 2", ["Thriller", "Crime"], "court case, novel writer, twist, family"),
        ("Kumbalangi Nights", ["Drama", "Family"], "four brothers, fishing village, love, dysfunctional"),
        ("Bangalore Days", ["Drama", "Romance"], "cousins, city life, marriage, dreams"),
        ("Premam", ["Romance", "Drama"], "three stages of love, malar teacher, butterflies"),
        ("Charlie", ["Adventure", "Drama"], "nomad, free spirit, graphic artist, mystery"),
        ("Maheshinte Prathikaaram", ["Comedy", "Drama"], "photographer, revenge without violence, shoes"),
        ("Uyare", ["Drama", "Thriller"], "acid attack, pilot dream, survival, toxic relation"),
        ("The Great Indian Kitchen", ["Drama", "Social"], "patriarchy, household chores, women rights"),
        ("Minnal Murali", ["Action", "Fantasy"], "superhero, lightning, village, villain"),
        ("Thallumaala", ["Action", "Comedy"], "fights, wedding, internet fame, style"),
        ("Jana Gana Mana", ["Drama", "Legal"], "courtroom, politics, media trial, twist"),
        ("Hridayam", ["Romance", "Drama"], "college, chennai, marriage, maturity"),
        ("Kannur Squad", ["Crime", "Thriller"], "police chase, investigation, team, road trip"),
    ]

    for t, g, k in malayalam_hits:
        movies.append(m(idx, t, g, "Malayalam", k, t))
        idx += 1

    # --- KANNADA (Sandalwood) ---
    kannada_hits = [
        ("KGF: Chapter 1", ["Action", "Crime"], "gold mines, rocky bhai, promise to mother"),
        ("KGF: Chapter 2", ["Action", "Crime"], "adheera, prime minister, empire, ocean"),
        ("Kantara", ["Thriller", "Fantasy"], "bhootakola, land issue, forest officer, scream"),
        ("777 Charlie", ["Adventure", "Drama"], "dog, depression, travel, snow, emotional"),
        ("Vikrant Rona", ["Fantasy", "Thriller"], "haunted village, police, jungle, mystery"),
        ("Sapta Sagaradaache Ello - Side A", ["Romance", "Drama"], "jail, lost love, cassette, ocean"),
        ("Garuda Gamana Vrishabha Vahana", ["Crime", "Drama"], "shiva, vishnu, mangalore, violence"),
        ("Ugramm", ["Action", "Thriller"], "srikanth, gangster, promise, violent"),
        ("Lucia", ["Sci-Fi", "Thriller"], "lucid dreaming, pill, theatre usher, superstar"),
        ("Rangitaranga", ["Thriller", "Mystery"], "pregnant wife, kamarottu, ghost, novelist"),
        ("Mungaru Male", ["Romance", "Drama"], "rain, rabbit, sacrifice, classic love"),
        ("Kirik Party", ["Comedy", "Drama"], "college engineering, senior junior, election"),
        ("James", ["Action", "Thriller"], "security agency, mafia, soldier, puneeth"),
        ("Robert", ["Action", "Drama"], "cook, gangster past, son sentiment"),
        ("Mufti", ["Action", "Crime"], "undercover cop, don, bhairathi ranagal"),
    ]

    for t, g, k in kannada_hits:
        movies.append(m(idx, t, g, "Kannada", k, t))
        idx += 1

    # --- ENGLISH (Hollywood) ---
    english_hits = [
        ("Inception", ["Sci-Fi", "Action"], "dreams, heist, subconscious, totem"),
        ("The Dark Knight", ["Action", "Crime"], "batman, joker, chaos, gotham"),
        ("Interstellar", ["Sci-Fi", "Adventure"], "black hole, time relativity, father daughter, corn"),
        ("Avengers: Endgame", ["Action", "Sci-Fi"], "thanos, time travel, snap, assemble"),
        ("Avengers: Infinity War", ["Action", "Sci-Fi"], "stones, snap, failure, sacrifice"),
        ("Avatar", ["Sci-Fi", "Adventure"], "pandora, blue aliens, nature, war"),
        ("Avatar: The Way of Water", ["Sci-Fi", "Adventure"], "oceans, whales, family protection"),
        ("Titanic", ["Romance", "Drama"], "shipwreck, iceberg, jack and rose, drawing"),
        ("The Matrix", ["Sci-Fi", "Action"], "simulation, red pill, neo, bullets"),
        ("The Godfather", ["Crime", "Drama"], "mafia family, offer you cant refuse, corleone"),
        ("Pulp Fiction", ["Crime", "Thriller"], "non-linear, burger, dance, briefcase"),
        ("The Shawshank Redemption", ["Drama", "Crime"], "prison escape, hope, friendship, rain"),
        ("Fight Club", ["Drama", "Thriller"], "soap, insomnia, underground club, twist"),
        ("Forrest Gump", ["Drama", "Romance"], "running, chocolates, history, innocence"),
        ("The Lion King", ["Animation", "Drama"], "simba, mufasa, hakuna matata, circle of life"),
        ("Joker", ["Drama", "Crime"], "mental illness, society, clown, stairs"),
        ("Barbie", ["Comedy", "Fantasy"], "dolls, real world, patriarchy, pink"),
        ("Oppenheimer", ["Drama", "History"], "atomic bomb, physics, trial, destroyer of worlds"),
        ("Dune: Part One", ["Sci-Fi", "Adventure"], "spice, desert, worms, paul atreides"),
        ("Dune: Part Two", ["Sci-Fi", "Action"], "holy war, prophecy, sand worms, emperor"),
        ("Spider-Man: No Way Home", ["Action", "Fantasy"], "multiverse, three spiders, forgetting"),
        ("Top Gun: Maverick", ["Action", "Drama"], "fighter jets, speed, mission, old school"),
        ("Mission: Impossible - Dead Reckoning", ["Action", "Thriller"], "ai entity, stunts, train, ethan hunt"),
        ("John Wick 4", ["Action", "Thriller"], "assassin, high table, guns, dogs"),
        ("Everything Everywhere All At Once", ["Sci-Fi", "Adventure"], "multiverse, bagel, mother daughter, kung fu"),
        ("Parasite", ["Thriller", "Drama"], "rich vs poor, basement, smell, korean"),
        ("Mad Max: Fury Road", ["Action", "Sci-Fi"], "desert chase, guitar, trucks, survival"),
        ("Gladiator", ["Action", "Drama"], "rome, general, arena, vengeance"),
        ("Jurassic Park", ["Sci-Fi", "Adventure"], "dinosaurs, amber, island, t-rex"),
        ("Harry Potter and the Sorcerer's Stone", ["Fantasy", "Adventure"], "wizard, hogwarts, magic, voldemort"),
    ]

    for t, g, k in english_hits:
        movies.append(m(idx, t, g, "English", k, t))
        idx += 1

    # Save
    if not os.path.exists('data'):
        os.makedirs('data')
        
    with open('data/movies.json', 'w') as f:
        json.dump(movies, f, indent=4)
        
    print(f"✅ Generated {len(movies)} REAL movies database.")

if __name__ == "__main__":
    generate_large_dataset()