import os
from core_scripts import read_file, write_file, compare_datasets

"""
Nature: sea*, ocean*, river, mountain, rain, snow, tree, sun, moon, world, Earth, forest, sky, plant, wind, soil/earth, 
flower, valley, root, lake, star, grass, leaf, air, sand, beach, wave, fire, ice, island, hill, heat, natureC

Math/Measurements: meter, centimeter, kilogram, inch, foot, pound, half, circle, square, temperature, date, weight, 
edge,corner
"""

NOUN_HEADER = 'German,English,Gender,Box,Passes,Fails\n'
ADJECTIVE_HEADER = 'German,English,Box,Passes,Fails\n'

noun_bank = {
    'Animal': [
        'Katze.Cat.F',
        'Hund.Dog.M',
        'Vogel.Bird.M',
        'Kuh.Cow.F',
        'Schwein.Pig.N',
        'Huhn.Chicken.N',
        'Fisch.Fish.M',
        'Pferd.Horse.N',
        'Kaninchen.Rabbit.N',
        'Bär.Bear.M',
        'Affe.Monkey.M',
        'Tier.Animal.N',
        'Wal.Whale.M',
        'Eule.Owl.F',
        'Maus.Mouse.F',
        'Elefant.Elephant.M',
        'Schaf.Sheep.N',
    ],
    'Transportation': [
        'Zug.Train.M',
        'Flugzeug.Plane.N',
        'Auto.Car.N',
        'Lastwagen.Truck.M',
        'Fahrrad.Bicycle|Bike.N',
        'Bus.Bus.M',
        'Boot.Boat.N',
        'Schiff.Ship.N',
        'Benzin.Fuel|Petrol.N',
        'Motor.Engine.M',
        'Bahnticket.Train Ticket.N',
        'Transport.Transportation.M',
        'Van.Van.M',
        'Motorrad.Motorbike|Motorcycle.N',
        'Roller.Scooter.M'
    ],
    'Location': [
        'Stadt.City|Town.F',
        'Haus.House.N',
        'Apartment.Apartment.N',
        'Straße.Street|Road.F',
        'Flughafen.Airport.M',
        'Hafen.Port.M',
        'Bahnhof.Train Station.M',
        'Brücke.Bridge.F',
        'Hotel.Hotel.N',
        'Restaurant.Restaurant.N',
        'Cafe.Cafe.N',
        'Bäckerei.Bakery.F',
        'Bauernhof.Farm.M',
        'Gericht.Court.N',
        'Schule.School.F',
        'Büro.Office.N',
        'Zimmer.Room.N',
        'Zoo.Zoo.M',
        'Universität.University.F',
        'Klub.Club.M',
        'Bar.Bar.F',
        'Park.Park.M',
        'Lager.Camp.N',
        'Geschäft.Store.N',
        'Geschäft.Shop.N',
        'Markt.Market.M',
        'Marktplatz.Marketplace.M',
        'Supermarkt.Supermarket.M',
        'Kino.Movie Theatre|Theatre.N',
        'Bibliothek.Library.F',
        'Krankenhaus.Hospital.N',
        'Polizeistation.Police Station.F',
        'Einkaufszentrum.Mall.N',
        'Kirche.Church.F',
        'Land.Country.N',
        'Weltraum.Outer Space|Space.M',
        'Bank.Bank.F',
        'Museum.Museum.N',
        'Apotheke.Pharmacy.F',
    ],
    'Clothing': [
        'Hut.Hat.M',
        'Kleid.Dress.N',
        'Anzug.Suit.M',
        'Rock.Skirt.M',
        'Hemd.Shirt.N',
        'T-shirt|Tshirt.T-shirt|Tshirt.N',
        'Hose.Pants.F',
        'Jeans.Jeans.F',
        'Shorts.Shorts.F',
        'Schuhe.Shoes.F',
        'Tasche.Pocket.F',
        'Mantel.Coat.M',
        'Fleck.Stain.M',
        'Kleidung.Clothes.F',
        'Gürtel.Belt.M',
        'Schal.Scarf.M',
        'Socken.Socks.F',
        'Pullover.Sweater.M'
    ],
    'Countries': [
        'Österreich.Austria.N',
        'Deutschland.Germany.N',
        'Schweiz.Switzerland.F',
        'Frankreich.France.N',
        'Spanien.Spain.N',
        'England.England.N',
        'Großbritannien.United Kingdom|UK.N',
        'Polen.Poland.N',
        'Belgien.Belgium.N',
        'Niederlande.Netherlands.N',
        'Italien.Italy.N',
        'Dänemark.Denmark.N',
        'Vereinigte Staaten.United States.N',
        'Kanada.Canada.N',
        'Mexiko.Mexico.N',
        'Brasilien.Brazil.N',
        'Japan.Japan.N',
        'China.China.N',
        'Indien.India.N',
        'Australien.Australia.N',
        'Neuseeland.New Zealand.N',
        'Russland.Russia.N',
        'Griechenland.Greece.N',
        'Amerika.America.N'
    ],
    # 'Nationalities': [
    #     'Österreicher.Austrian.M',
    #     'Deutsch.German.N',
    #
    #     'Switzerland.Schweiz.F',
    #     'Frankreich.France.N',
    #     'Spanien.Spain.N',
    #     'England.England.N',
    #     'Vereinigte Königreich.United Kingdom.N',
    #     'Polen.Poland.N',
    #     'Belgien.Belgium.N',
    #     'Niederlande.Netherlands.N',
    #     'Italien.Italy.N',
    #     'Dänemark.Denmark.N',
    #     'Vereinigte Staaten.United States.N',
    #     'Kanada.Canada.N',
    #     'Mexiko.Mexico.N',
    #     'Brasilien.Brazil.N',
    #     'Japan.Japan.N',
    #     'China.China.N',
    #     'Indien.India.N',
    #     'Australien.Australia.N',
    #     'Neuseeland.New Zealand.N',
    #     'Russland.Russia.N',
    #     'Griechenland.Greece.N',
    #     'Amerika.America.N'
    # ],
    'Home': [
        'Couch.Couch.F',
        'Bett.Bed.N',
        'Stuhl.Chair.M',
        'Tisch.Table.M',
        'Teppich.Carpet.M',
        'Bücherregal.Bookshelf|Bookcase.N',
        'Fenster.Window.N',
        'Tür.Door.F',
        'Schlafzimmer.Bedroom.N',
        'Küche.Kitchen.F',
        'Toilette.Toilet.F',
        'Badezimmer.Bathroom.N',
        'Dusche.Shower.F',
        'Bleistift.Pencil.M',
        'Stift.Pen.M',
        'Foto.Photo.N',
        'Buch.Book.N',
        'Seite.Page.F',
        'Schlüssel.Key.M',
        'Mauer.Wall.F',
        'Boden.Floor.M',
        'Pool.Pool.M',
        'Schloss.Lock.N',
        'Garten.Garden.M',
        'Tasche.Bag.F',
        'Kiste.Box.F',
        'Werkzeug.Tool.N',
        'Schreibtisch.Desk.M',
    ],
    'People': [
        'Sohn.Son.M',
        'Tochter.Daughter.F',
        'Mutter.Mother.F',
        'Vater.Father.M',
        'Elternteil.Parent.N',
        'Baby.Baby.N',
        'Mann.Man|Husband.M',
        'Frau.Women|Wife|Ms|Mrs.F',
        'Bruder.Brother.M',
        'Schwester.Sister.F',
        'Familie.Family.F',
        'Oma.Grandma.F',
        'Opa.Grandpa.M',
        'Junge.Boy.M',
        'Mädchen.Girl.N',
        'Kind.Child.N',
        'Erwachsene.Adult.M',
        'Nachbar.Neighbor.M',
        'Person.Person.F',
        'Mensch.Human.M',
        'Onkel.Uncle.M',
        'Tante.Aunt.F',
        'Freund.Friend(m).M',
        'Freundin.Friend(f).F',
        'Partner.Partner(m).M',
        'Partnerin.Partner(f).F',
        'Mitbewohner.Roommate(m).M',
        'Mitbewohnerin.Roommate(f).F',
        'Herr.Mr.M'
    ],
    'Job': [
        'Lehrer.Teacher(m).M',
        'Lehrerin.Teacher(f).F',
        'Student.Student(m).M',
        'Studentin.Student(f).F',
        'Anwalt.Lawyer(m).M',
        'Anwältin.Lawyer(f).F',
        'Arzt.Doctor(m).M',
        'Ärztin.Doctor(f).F',
        'Kellner.Waiter.M',
        'Kellnerin.Waitress.F',
        'Polizist.Policeman.M',
        'Polizistin.Policewoman.F',
        'Künstler.Artist(m).M',
        'Künstlerin.Artist(F).F',
        'Autor.Author(m).M',
        'Autorin.Author(f).F',
        'Schauspieler.Actor.M',
        'Schauspielerin.Actress.F',
        'Arbeit.Job.F',
        'Ingenieur.Engineer(m).M',
        'Ingenieurin.Engineer(f).F',
        'Professor.Professor(m).M',
        'Professorin.Professor(f).F'
    ],
    'Beverages': [
        'Kaffee.Coffee.M',
        'Tee.Tea.M',
        'Wasser.Water.N',
        'Wein.Wine.M',
        'Bier.Beer.M',
        'Saft.Juice.M',
        'Milch.Milk.F',
        'Trinken.Drink.N',
        'Espresso.Espresso.M',
        'Cappuccino.Cappuccino.M',
        'Mineralwasser.Mineral Water.N',
        'Rotwein.Red Wine.M',
    ],
    'Food': [
        'Ei.Egg.N',
        'Käse.Cheese.M',
        'Brot.Bread.N',
        'Suppe.Soup.F',
        'Kuchen.Cake.M',
        'Schweinefleisch.Pork.N',
        'Fleisch.Meat.N',
        'Lamm.Lamb.N',
        'Apfel.Apple.M',
        'Banane.Banana.F',
        'Orange.Orange.F',
        'Zitrone.Lemon.F',
        'Mais.Corn.M',
        'Reis.Rice.M',
        'Öl.Oil.N',
        'Zucker.Sugar.M',
        'Salz.Salt.N',
        'Essen.Food.N',
        'Wurst.Sausage.F',
        'Schnitzel.Schnitzel.F',
        'Sandwich.Sandwich.N',
        'Salat.Salad.M',
        'Obstsalat.Fruit Salad.M',
        'Pizza.Pizza.F',
        'Döner.Doner Kebab.M',
        'Tomate.Tomato.F'
    ],
    'DaysOfWeek': [
        'Montag.Monday.M',
        'Dienstag.Tuesday.M',
        'Mittwoch.Wednesday.M',
        'Donnerstag.Thursday.M',
        'Freitag.Friday.M',
        'Samstag.Saturday.M',
        'Sonntag.Sunday.M',
    ],
    'Months': [
        'Januar.January.M',
        'Februar.February.M',
        'März.March.M',
        'April.April.M',
        'Mai.May.M',
        'Juni.June.M',
        'Juli.July.M',
        'August.August.M',
        'September.September.M',
        'Oktober.October.M',
        'November.November.M',
        'Dezember.December.M',
    ],
    'Time': [
        'Jahr.Year.N',
        'Monat.Month.M',
        'Woche.Week.F',
        'Heute.Today.N',
        'Wochenende.Weekend.N',
        'Wochentag.Weekday.M',
        'Tag.Day.M',
        'Stunde.Hour.F',
        'Minute.Minute.F',
        'Sekunde.Second.F',
        'Morgen.Morning.M',
        'Nachmittag.Afternoon.M',
        'Abend.Evening.M',
        'Nacht.Night.F',
        'Zeit.Time.F',
    ],
    'Weather': [
        'Sommer.Summer.M',
        'Winter.Winter.M',
        'Frühling.Spring.M',
        'Herbst.Autumn.M'
    ],
    'Electronics': [
        'Uhr.Clock.F',
        'Lampe.Lamp.F',
        'Fan.Fan.M',
        'Handy.Cellphone|Phone.N',
        'Internet.Internet.N',
        'Computer.Computer.M',
        'Programm.Program.N',
        'Laptop.Laptop.M',
        'Bildschirm.Screen.M',
        'Kamera.Camera.F',
        'Fernsehen.Television|TV.N',
        'Radio.Radio.N'
    ],
    'Body': [
        'Kopf.Head.M',
        'Hals.Neck.M',
        'Gesicht.Face.N',
        'Bart.Beard.M',
        'Haar.Hair.N',
        'Auge.Eye.N',
        'Mund.Mouth.M',
        'Lippe.Lip.F',
        'Nase.Nose.F',
        'Zahn.Tooth.M',
        'Ohr.Ear.N',
        'Zunge.Tongue.F',
        'Rücken.Back.M',
        'Zeh.Toe.M',
        'Finger.Finger.M',
        'Fuß.Foot.M',
        'Hand.Hand.F',
        'Bein.Leg.N',
        'Arm.Arm.M',
        'Schulter.Shoulder.F',
        'Herz.Heart.N',
        'Blut.Blood.N',
        'Gehirn.Brain.N',
        'Knie.Knee.N',
        'Schweiß.Sweat.M',
        'Krankheit.Disease.F',
        'Knochen.Bone.M',
        'Stimme.Voice.F',
        'Haut.Skin.F',
        'Körper.Body.M',
    ],
    'Nature': [
        'Sonne.Sun.F',
        'Mond.Moon.M',
        'Regen.Rain.M',
        'Schnee.Snow.M',
        'Wolke.Cloud.F'
    ],
    'Materials': [
        'Glas.Glass.N',
        'Metall.Metal.N',
        'Kunststoff.Plastic.M',
        'Holz.Wood.N',
        'Stein.Stone.M',
        'Diamant.Diamond.M',
        'Gold.Gold.N',
        'Kupfer.Copper.N',
        'Silber.Silver.N'
    ],
    'Measurements': [],
    'Sport': [
        'Fußball.Football.M',
        'Basketball.Basketball.M',
        'Tennis.Tennis.N',
        'Klettern.Climbing.N',
        'Bouldern.Bouldering.N',
        'Volleyball.Volleyball.M',
        'Rugby.Rugby.N',
        'Sport.Sport.M',
        'Spiel.Game.N',
    ],
    'Misc': [
        'Karte.Map.F',
        'Klang.Sound.M',
        'Bild.Image.N',
        'Sonnencreme.Suncream.F',
        'Geld.Money.N',
        'Geldautomat.ATM.M',
        'Euro.Euro.M',
    ],
}


LETTERS = 'üäßö'

misc_bank = {
    'Colour': [
        'Rot.Red',
        'Gelb.Yellow',
        'Blau.Blue',
        'Orange.Orange',
        'Grün.Green',
        'Lila.Purple',
        'Rosa.Pink',
        'Braun.Brown',
        'Grau.Grey|Gray',
        'Schwarz.Black',
        'Weiß.White',
        'Beige.Beige'
    ],
    'Adjectives': [
        'Lang.Long',
        'Süß.Sweet',
        'Kurz.Short',
        'groß.Tall|Big|Large',
        'Breit.Wide',
        'Modern.Modern',
        'Klein.Small',
        'Wenig.Little',
        'Langsam.Slow',
        'Schnell.Fast',
        'Heiß.Hot',
        'Kalt.Cold',
        'Warm.Warm',
        'Kühl|Cool.Cool',
        'Neu.New',
        'Alt.Old',
        'Jung.Young',
        'Gut.Good',
        'Schlecht.Bad',
        'Nass.Wet',
        'Trocken.Dry',
        'Krank.Sick',
        'Gesund.Healthy',
        'Laut.Loud',
        'Ruhig.Quiet',
        'Glücklich.Happy',
        'Traurig.Sad',
        'Schön.Beautiful',
        'Hässlich.Ugly',
        'Taub.Deaf',
        'Blind.Blind',
        'Nett.Nice',
        'Gemein.Mean',
        'Reich.Rich',
        'Arm.Poor',
        'Teuer.Expensive',
        'Billig.Cheap',
        'Eng.Tight',
        'Lose.Loose',
        'Hoch.High',
        'Niedrig.Low',
        'Weich.Soft',
        'Hart.Hard',
        'Tief.Deep',
        'Seicht.Shallow',
        'Sauber.Clean',
        'Schmutzig.Dirty',
        'Stark.Strong',
        'Schwach.Weak',
        'Tot.Dead',
        'Lebendig.Alive',
        'Schwer.Heavy',
        'Licht.Light(weight)',
        'Dunkel.Dark',
        'Hell.Light',
        'Interessant.Interesting',
        'Nervös.Nervous',
        'Wunderbar.Wonderful',
        'Toll|Super.Great',
        'Perfekt.Perfect',
        'Lecker.Delicious',
        'Elegant.Elegant',
        'Aus.Off',
        'Stressig.Stressful',
        'Frei.Free',
        'Fantastisch.Fantastic',
    ],
    'Pronouns': [  # TODO rethink this
        'Ich.I',
        'Du.You(informal)',
        'Sie.You(formal)',
        'Er.He',
        'Sie.She',
        'Es.It',
        'Wir.We',
        'Ihr.You All(informal)',
        'Sie.You All(formal)',
        'sie.They'
    ],
    'CommonSayings': [
        'Hallo.Hello',
        'Danke.Thank You',
        'Guten Tag.Good Day',
        'Guten Morgen.Good Morning',
        'Guten Nachmittag.Good Afternoon',
        'Guten Abend.Good Evening',
        'Guten Nacht.Good Night',
        'Entschuldigung.Sorry',
        'Auf Wiedersehen.Goodbye',
        'Ja.Yes',
        'Nein.No',
        'Ok.Ok',
        'Prost.Cheers',
        'Bitte.Please',
        'Vielen Dank.Thank You Very Much',
        'Kein Problem.No Problem'
    ],
    'Conjunctions': [
        'Aber.But',
        'Und.And',
        'Oder.Or',
        'Als.As',
        'Denn.Because',
        'Wenn.If',

    ],
    'Prepositions': [
        'Für.For',
        'Zu.To',
        'Mit.With'
    ],
    'Adverbs': [
        'Sehr.Very',
        'Hier.Here',
        'Dort.There',
        'Wo.Where',
        'Warum.Why',
        'Wie.How',
        'Was.What',
        'Jetzt.Now',
        'Wirklich.Really',
        'Circa.Approximately',
    ],
    'MISC': [
        'Der.The(m)',
        'Die.The(f)',
        'Das.The(n)',
        'Ein.A(m)',
        'Eine.A(f)',
    ]
}

number_cache_ger = {
    '0': 'Null',
    '1': 'Ein',
    '2': 'Zwei',
    '3': 'Drei',
    '4': 'Vier',
    '5': 'Fünf',
    '6': 'Sechs',
    '7': 'Sieben',
    '8': 'Acht',
    '9': 'Neun',
    '10': 'Zehn',
    '11': 'Elf',
    '12': 'Zwölf',
    '13': 'Dreizehn',
    '14': 'Vierzehn',
    '15': 'Fünfzehn',
    '16': 'Sechzehn',
    '17': 'Siebzehn',
    '18': 'Achtzehn',
    '19': 'Neunzehn',
    '20': 'Zwanzig',
    '30': 'Dreißig',
    '40': 'Vierzig',
    '50': 'Fünfzig',
    '60': 'Sechzig',
    '70': 'Siebzig',
    '80': 'Achtzig',
    '90': 'Neunzig',
    '100': 'Hundert'
}

NOUN_PATH = './../Datenbank/Wörter/Nouns/'
MISC_PATH = './../Datenbank/Wörter/Other/'


def write_nouns():
    noun_files = os.listdir(NOUN_PATH)
    for category, words_list in noun_bank.items():
        if category + '.csv' in noun_files:
            print("File already exists")
            file_data = read_file(f"{NOUN_PATH}{category}.csv")
            existing_words = [x.split(',')[0] for x in file_data[1:]]
        else:
            file_data = [NOUN_HEADER]
            existing_words = []
        for word_data in words_list:
            try:
                german, english, gender = word_data.split('.')
                german = german.capitalize()
                english = english.capitalize()
                gender = gender.capitalize()
                if gender not in ['M', 'F', 'N']:
                    print(word_data)
                    raise Exception("Invalid gender")
                if german not in existing_words:
                    new_line = f"{german},{english},{gender},0,0,0\n"
                    file_data.append(new_line)
            except ValueError as err:
                print(word_data)
                raise err
        write_file(file_data, f"{NOUN_PATH}{category}.csv")


def write_other():
    adjective_files = os.listdir(MISC_PATH)
    for category, words_list in misc_bank.items():
        if category + '.csv' in adjective_files:
            print("File already exists")
            file_data = read_file(f"{MISC_PATH}{category}.csv")
            existing_words = [x.split(',')[0] for x in file_data[1:]]
        else:
            file_data = [ADJECTIVE_HEADER]
            existing_words = []
        for word_data in words_list:
            try:
                german, english = word_data.split('.')
                german = german.capitalize()
                english = english.capitalize()
                if german not in existing_words:
                    new_line = f"{german},{english},0,0,0\n"
                    file_data.append(new_line)
            except ValueError as err:
                print(word_data)
                raise err
        write_file(file_data, f"{MISC_PATH}{category}.csv")


def write_numbers():
    file_data = [NOUN_HEADER]
    i = 0
    bonus_lines = [
        'Eintausend,1000,F,0,0,0\n',
        'Erst,1st,F,0,0,0\n',
        'Zweite,2nd,F,0,0,0\n',
        'Dritte,3rd,F,0,0,0\n',
        'Vierte,4th,F,0,0,0\n',
        'Fünfte,5th,F,0,0,0\n',
        'Sechste,6th,F,0,0,0\n',
        'Siebte,7th,F,0,0,0\n',
        'Achte,8th,F,0,0,0\n',
        'Neunte,9th,F,0,0,0\n',
        'Zehnte,10th,F,0,0,0\n',
    ]
    while i < 115:
        # german words
        if str(i) in number_cache_ger:
            g_out = number_cache_ger[str(i)]
            if i == 1:
                g_out += 's'
        elif i >= 100:
            new = str(i - 100)
            g_out = f"einhundertund{number_cache_ger[new]}"
        else:
            tens = f"{i // 10}0"
            ones = i % 10
            g_out = f'{number_cache_ger[str(ones)]}und{number_cache_ger[tens]}'
        line = f"{g_out.capitalize()},{i},F,0,0,0\n"
        file_data.append(line)
        i += 1
    file_data += bonus_lines
    write_file(file_data, f"{MISC_PATH}Numbers.csv")


def write_words():
    write_nouns()
    write_other()
    write_numbers()
    pass


write_words()

if __name__ == '__main__':
    base_dir = './../Datenbank/Wörter/Nouns/'
    other_files = [
        './../Datenbank/Wörter/Other/Adjectives.csv',
        './../Datenbank/Wörter/Other/Colour.csv',
        './../Datenbank/Wörter/Other/Pronouns.csv',
        './../Datenbank/Wörter/Other/CommonSayings.csv',
        './../Datenbank/Wörter/Other/Conjunctions.csv',
        './../Datenbank/Wörter/Other/Prepositions.csv',
        './../Datenbank/Wörter/Other/Adverbs.csv',
        './../Datenbank/Wörter/Other/MISC.csv',
    ]

    new_files = [base_dir + x for x in os.listdir(base_dir)] + other_files
    old_files = ['./../Datenbank/master_word_bank.csv']
    # old_files = ['./../Datenbank/Wörter/food.csv']
    compare_datasets(old_files, new_files)
