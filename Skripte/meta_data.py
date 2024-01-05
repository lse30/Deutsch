word_files = [
    ('Animal', './../Datenbank/Wörter/Nouns/Animal.csv'),
    ('Beverages', './../Datenbank/Wörter/Nouns/Beverages.csv'),
    ('Body', './../Datenbank/Wörter/Nouns/Body.csv'),
    ('Clothing', './../Datenbank/Wörter/Nouns/Clothing.csv'),
    ('Countries', './../Datenbank/Wörter/Nouns/Countries.csv'),
    ('DaysOfWeek', './../Datenbank/Wörter/Nouns/DaysOfWeek.csv'),
    ('Electronics', './../Datenbank/Wörter/Nouns/Electronics.csv'),
    ('Food', './../Datenbank/Wörter/Nouns/Food.csv'),
    ('Home', './../Datenbank/Wörter/Nouns/Home.csv'),
    ('Job', './../Datenbank/Wörter/Nouns/Job.csv'),
    ('Location', './../Datenbank/Wörter/Nouns/Location.csv'),
    ('Materials', './../Datenbank/Wörter/Nouns/Materials.csv'),
    ('Measurements', './../Datenbank/Wörter/Nouns/Measurements.csv'),
    ('Misc', './../Datenbank/Wörter/Nouns/Misc.csv'),
    ('Months', './../Datenbank/Wörter/Nouns/Months.csv'),
    ('Nature', './../Datenbank/Wörter/Nouns/Nature.csv'),
    ('People', './../Datenbank/Wörter/Nouns/People.csv'),
    ('Sport', './../Datenbank/Wörter/Nouns/Sport.csv'),
    ('Time', './../Datenbank/Wörter/Nouns/Time.csv'),
    ('Transportation', './../Datenbank/Wörter/Nouns/Transportation.csv'),
    ('Weather', './../Datenbank/Wörter/Nouns/Weather.csv'),
    ('Adjectives', './../Datenbank/Wörter/Other/Adjectives.csv'),
    ('Adverbs', './../Datenbank/Wörter/Other/Adverbs.csv'),
    ('Colour', './../Datenbank/Wörter/Other/Colour.csv'),
    ('CommonSayings', './../Datenbank/Wörter/Other/CommonSayings.csv'),
    ('Conjunctions', './../Datenbank/Wörter/Other/Conjunctions.csv'),
    ('Prepositions', './../Datenbank/Wörter/Other/Prepositions.csv'),
]

LETTERS = 'üäßö'

noun_bank = {
    'Animal': [
        'Katze.Cat.F',
        'Kätzchen.Kitten.N',
        'Löwe.Lion.M',
        'Löwin.Lioness.F',
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
        'Flugzeug.Plane|Aeroplane|Airplane.N',
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
        'Konzert.Concert.N',
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
        'Stadtzentrum.City Centre|City Center.N'
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
        'HandTasche.Handbag|Purse.F'
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
        'Tasse.Cup.F',
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
        'Flasche.Bottle.F',
        'Kiste.Box.F',
        'Zeitung.Newspaper.F',
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
        'Nachbar.Neighbour|Neighbor.M',
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
        'Wolke.Cloud.F',
        'Meer.Sea.N',
        'Ozean.Ocean.M',
        'Fluss.River.M',
        'Berg.Mountain.M',
        'Baum.Tree.M',
        'Welt.World.F',
        'Erde.Earth.F',
        'Wald.Forest.M',
        'Himmel.Sky.M',
        'Pflanze.Plant.F',
        'Wind.Wind.M',
        'Boden.Soil.M',
        'Blume.Flower.F',
        'Tal.Valley.N',
        'See.Lake.M',
        'Stern.Star.M',
        'Gras.Grass.N',
        'Blatt.Leaf.N',
        'Luft.Air.F',
        'Sand.Sand.M',
        'Strand.Beach.M',
        'Welle.Wave.F',
        'Feuer.Fire.N',
        'Eis.Ice.N',
        'Insel.Island.F',
        'Hügel.Hill.M'
    ],
    'Materials': [
        'Glas.Glass.N',
        'Metall.Metal.N',
        'Plastik.Plastic.N',
        'Holz.Wood.N',
        'Stein.Stone.M',
        'Papier.Paper.N',
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
        'Sonnencreme.Suncream|Sunscreen.F',
        'Geld.Money.N',
        'Geldautomat.ATM.M',
        'Euro.Euro.M',
        'Rechnung.Check.F',
        'Nummer.Number.F'
    ],
}

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
        'Licht.Light',
        'Dunkel.Dark',
        'Hell.Bright',
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
        'Entschuldigung.Excuse Me|Sorry',
        'Es Tut Mir Leid.I Am Sorry|Sorry|Im Sorry',
        'Auf Wiedersehen.Goodbye',
        'Tschüss.Bye|Goodbye',
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
        'Durch.Through',
        'Entlang.Along',
        'Gegen.Against|Around',
        'Ohne.Without',
        'Um.Round|Around',
        'Wider.Against|Contrary To',
        'Zu.To',
        'Mit.With',
        'An.At',
        'Auf.On|To|At',
        'Hinter.Behind',
        'In.In',
        'Neben.Next To|Besides',
        'Über.Over|Across|Above',
        'Unter.Under|Among',
        'Vor.In Front Of|Before',
        'Zwischen.Between'
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
        'Links.Left|To The Left',
        'Rechts.Right|To The Right'
    ],
    'MISC': [
        'Der.The(m)',
        'Die.The(f)',
        'Das.The(n)',
        'Ein.A(m)',
        'Eine.A(f)',
    ]
}
