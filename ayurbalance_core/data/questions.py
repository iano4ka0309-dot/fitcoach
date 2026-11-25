PRAKRITI_QUESTIONS = [

    # ── БЛОК 1: ТІЛО ──────────────────────────────────────
    {                              # відкрили питання 1
        "id": 1,
        "category": "body",        # просто рядок!
        "category_name": {         # відкрили category_name
            "ua": "🏃 Будова тіла",
            "pl": "🏃 Budowa ciała",
            "en": "🏃 Body Build",
        },                         # закрили category_name
        "short": True,
        "question": {              # відкрили question
            "ua": "Яка у вас статура від природи?",
            "pl": "Jaka jest Twoja statura od urodzenia?",
            "en": "What is your natural body type?",
        },                         # закрили question
        "options": {               # відкрили options
            "vata": {              # відкрили vata
                "ua": "Худорляве, тонкі кістки, важко набрати вагу",
                "pl": "Szczupła, cienkie kości, trudno przybrać na wadze",
                "en": "Slim, thin bones, hard to gain weight",
            },                     # закрили vata
            "pitta": {             # відкрили pitta
                "ua": "Середнє, пропорційне, є м'язи",
                "pl": "Średnia, proporcjonalna, jest umięśnienie",
                "en": "Medium, proportional, muscular",
            },                     # закрили pitta
            "kapha": {             # відкрили kapha
                "ua": "Щільне або велике, широкі кістки, легко набираю вагу",
                "pl": "Masywna lub duża, szerokie kości, łatwo przybieram",
                "en": "Large or dense, wide bones, easy to gain weight",
            },                     # закрили kapha
        },                         # закрили options
    },                             # закрили питання 1

    {                              # відкрили питання 2
        "id": 2,
        "category": "body",
        "category_name": {
            "ua": "🏃 Будова тіла",
            "pl": "🏃 Budowa ciała",
            "en": "🏃 Body Build",
        },
        "short": False,
        "question": {
            "ua": "Як змінюється ваша вага протягом життя?",
            "pl": "Jak zmienia się Twoja waga przez życie?",
            "en": "How does your weight change throughout your life?",
        },
        "options": {
            "vata": {
                "ua": "Важко набрати, легко схуднути, вага нестабільна",
                "pl": "Trudno przybrać, łatwo schudnąć, waga niestabilna",
                "en": "Hard to gain, easy to lose, unstable weight",
            },
            "pitta": {
                "ua": "Легко і набираю і скидаю, вага керована",
                "pl": "Łatwo i przybieram i chudnę, waga kontrolowana",
                "en": "Easy to gain and lose, weight is manageable",
            },
            "kapha": {
                "ua": "Легко набираю, дуже важко схуднути",
                "pl": "Łatwo przybieram, bardzo trudno schudnąć",
                "en": "Easy to gain weight, very hard to lose it",
            },
        },
    },                             # закрили питання 2

    {                              # відкрили питання 3
        "id": 3,
        "category": "body",
        "category_name": {
            "ua": "🏃 Будова тіла",
            "pl": "🏃 Budowa ciała",
            "en": "🏃 Body Build",
        },
        "short": False,
        "question": {
            "ua": "Які у вас суглоби та кістки?",
            "pl": "Jakie masz stawy i kości?",
            "en": "What are your joints and bones like?",
        },
        "options": {
            "vata": {
                "ua": "Дрібні суглоби, тонкі кістки, буває хрускіт",
                "pl": "Małe stawy, cienkie kości, czasem chrzęst",
                "en": "Small joints, thin bones, sometimes creaking",
            },
            "pitta": {
                "ua": "Середні суглоби, помірний розвиток",
                "pl": "Średnie stawy, umiarkowany rozwój",
                "en": "Medium joints, moderate development",
            },
            "kapha": {
                "ua": "Великі суглоби, широкі кістки, добре розвинені",
                "pl": "Duże stawy, szerokie kości, dobrze rozwinięte",
                "en": "Large joints, wide bones, well-developed",
            },
        },
    },                             # закрили питання 3
    # ── БЛОК 2: ШКІРА ──────────────────────────────────────
    # ── БЛОК 2: ШКІРА (питання 4-6) ──────────────────────
    {
        "id": 4,
        "category": "skin",
        "category_name": {
            "ua": "✨ Шкіра",
            "pl": "✨ Skóra",
            "en": "✨ Skin",
        },
        "short": True,
        "question": {
            "ua": "Який у вас тип шкіри від природи?",
            "pl": "Jaki jest Twój naturalny typ skóry?",
            "en": "What is your natural skin type?",
        },
        "options": {
            "vata": {
                "ua": "Суха, шорстка, схильна до лущення",
                "pl": "Sucha, szorstka, skłonna do łuszczenia",
                "en": "Dry, rough, prone to flaking",
            },
            "pitta": {
                "ua": "Ніжна, чутлива, тепла, схильна до почервоніння",
                "pl": "Delikatna, wrażliwa, ciepła, skłonna do zaczerwienień",
                "en": "Delicate, sensitive, warm, prone to redness",
            },
            "kapha": {
                "ua": "Жирна або змішана, гладка, прохолодна",
                "pl": "Tłusta lub mieszana, gładka, chłodna",
                "en": "Oily or combination, smooth, cool",
            },
        },
    },

    {
        "id": 5,
        "category": "skin",
        "category_name": {
            "ua": "✨ Шкіра",
            "pl": "✨ Skóra",
            "en": "✨ Skin",
        },
        "short": False,
        "question": {
            "ua": "Як ваша шкіра реагує на сонце?",
            "pl": "Jak Twoja skóra reaguje na słońce?",
            "en": "How does your skin react to the sun?",
        },
        "options": {
            "vata": {
                "ua": "Шкіра суха, сонце висушує ще більше, нерівномірний тон",
                "pl": "Skóra sucha, słońce wysusza bardziej, nierównomierny kolor",
                "en": "Skin is dry, sun dries it further, uneven skin tone",
            },
            "pitta": {
                "ua": "Легко обгораю, шкіра червоніє, з'являються плями",
                "pl": "Łatwo się oparzam, skóra czerwienieje, pojawiają się plamy",
                "en": "Burn easily, skin reddens, spots appear",
            },
            "kapha": {
                "ua": "Добре переносить сонце, рідко обгорає, засмага рівномірна",
                "pl": "Dobrze znosi słońce, rzadko się opala, równomierna opalenizna",
                "en": "Tolerates sun well, rarely burns, tans evenly",
            },
        },
    },

    {
        "id": 6,
        "category": "skin",
        "category_name": {
            "ua": "✨ Шкіра",
            "pl": "✨ Skóra",
            "en": "✨ Skin",
        },
        "short": False,
        "question": {
            "ua": "Як ви пітнієте?",
            "pl": "Jak się pocisz?",
            "en": "How do you sweat?",
        },
        "options": {
            "vata": {
                "ua": "Мало, шкіра часто суха навіть у спеку",
                "pl": "Mało, skóra często sucha nawet w upale",
                "en": "Little, skin often dry even in heat",
            },
            "pitta": {
                "ua": "Рясно, навіть при незначному навантаженні",
                "pl": "Obficie, nawet przy niewielkim wysiłku",
                "en": "Profusely, even with minimal effort",
            },
            "kapha": {
                "ua": "Помірно, пітнію рівномірно",
                "pl": "Umiarkowanie, pocę się równomiernie",
                "en": "Moderately, sweat evenly",
            },
        },
    },
    # ── БЛОК 3: ВОЛОССЯ (питання 7-9) ─────────────────────
    {
        "id": 7,
        "category": "hair",
        "category_name": {
            "ua": "💇 Волосся",
            "pl": "💇 Włosy",
            "en": "💇 Hair",
        },
        "short": True,
        "question": {
            "ua": "Яке у вас волосся від природи?",
            "pl": "Jakie masz włosy z natury?",
            "en": "What is your hair like naturally?",
        },
        "options": {
            "vata": {
                "ua": "Сухе, ламке, кучеряве або хвилясте",
                "pl": "Suche, łamliwe, kręcone lub faliste",
                "en": "Dry, brittle, curly or wavy",
            },
            "pitta": {
                "ua": "Тонке, пряме, м'яке, рання сивина або облисіння",
                "pl": "Cienkie, proste, miękkie, wczesna siwizna lub łysienie",
                "en": "Fine, straight, soft, early greying or hair loss",
            },
            "kapha": {
                "ua": "Густе, жирне, блискуче, повільно росте",
                "pl": "Gęste, tłuste, błyszczące, wolno rośnie",
                "en": "Thick, oily, shiny, slow growing",
            },
        },
    },

    {
        "id": 8,
        "category": "hair",
        "category_name": {
            "ua": "💇 Волосся",
            "pl": "💇 Włosy",
            "en": "💇 Hair",
        },
        "short": False,
        "question": {
            "ua": "Який у вас колір волосся від природи?",
            "pl": "Jaki jest Twój naturalny kolor włosów?",
            "en": "What is your natural hair color?",
        },
        "options": {
            "vata": {
                "ua": "Темне — чорне або темно-коричневе",
                "pl": "Ciemne — czarne lub ciemnobrązowe",
                "en": "Dark — black or dark brown",
            },
            "pitta": {
                "ua": "Руде, світло-коричневе або з рудуватим відтінком",
                "pl": "Rude, jasnobrązowe lub z rudawym odcieniem",
                "en": "Red, light brown or with reddish tint",
            },
            "kapha": {
                "ua": "Темно-коричневе або чорне, густе і блискуче",
                "pl": "Ciemnobrązowe lub czarne, gęste i błyszczące",
                "en": "Dark brown or black, thick and shiny",
            },
        },
    },

    {
        "id": 9,
        "category": "hair",
        "category_name": {
            "ua": "💇 Волосся",
            "pl": "💇 Włosy",
            "en": "💇 Hair",
        },
        "short": False,
        "question": {
            "ua": "Як поводиться ваша шкіра голови?",
            "pl": "Jak zachowuje się skóra głowy?",
            "en": "How is your scalp?",
        },
        "options": {
            "vata": {
                "ua": "Суха, схильна до лупи сухого типу",
                "pl": "Sucha, skłonna do suchego łupieżu",
                "en": "Dry, prone to dry dandruff",
            },
            "pitta": {
                "ua": "Чутлива, схильна до запалень, жирна лупа",
                "pl": "Wrażliwa, skłonna do stanów zapalnych, tłusty łupież",
                "en": "Sensitive, prone to inflammation, oily dandruff",
            },
            "kapha": {
                "ua": "Жирна, схильна до жирної лупи",
                "pl": "Tłusta, skłonna do tłustego łupieżu",
                "en": "Oily, prone to oily dandruff",
            },
        },
    },
    # ── БЛОК 4: АПЕТИТ (питання 10-12) ───────────────────
    {
        "id": 10,
        "category": "appetite",
        "category_name": {
            "ua": "🍽️ Апетит та травлення",
            "pl": "🍽️ Apetyt i trawienie",
            "en": "🍽️ Appetite and digestion",
        },
        "short": True,
        "question": {
            "ua": "Який у вас апетит?",
            "pl": "Jaki masz apetyt?",
            "en": "How is your appetite?",
        },
        "options": {
            "vata": {
                "ua": "Нерегулярний, мінливий, часто забуваю поїсти",
                "pl": "Nieregularny, zmienny, często zapominam o jedzeniu",
                "en": "Irregular, variable, often forget to eat",
            },
            "pitta": {
                "ua": "Сильний, якщо не поїм вчасно — дратуюсь",
                "pl": "Silny, jeśli nie zjem na czas — denerwuję się",
                "en": "Strong, if I don't eat on time I get irritable",
            },
            "kapha": {
                "ua": "Помірний, стабільний, можу пропустити їжу",
                "pl": "Umiarkowany, stabilny, mogę pominąć posiłek",
                "en": "Moderate, stable, can skip meals easily",
            },
        },
    },

    {
        "id": 11,
        "category": "appetite",
        "category_name": {
            "ua": "🍽️ Апетит та травлення",
            "pl": "🍽️ Apetyt i trawienie",
            "en": "🍽️ Appetite and digestion",
        },
        "short": False,
        "question": {
            "ua": "Як ви перетравлюєте їжу?",
            "pl": "Jak trawisz jedzenie?",
            "en": "How do you digest food?",
        },
        "options": {
            "vata": {
                "ua": "Нерегулярно, буває здуття і гази",
                "pl": "Nieregularnie, zdarzają się wzdęcia i gazy",
                "en": "Irregularly, bloating and gas occur",
            },
            "pitta": {
                "ua": "Швидко і добре, але буває печія або кислота",
                "pl": "Szybko i dobrze, ale zdarza się zgaga lub kwasowość",
                "en": "Quickly and well, but heartburn or acidity may occur",
            },
            "kapha": {
                "ua": "Повільно, відчуття важкості після їжі",
                "pl": "Powoli, uczucie ciężkości po jedzeniu",
                "en": "Slowly, feeling of heaviness after eating",
            },
        },
    },

    {
        "id": 12,
        "category": "appetite",
        "category_name": {
            "ua": "🍽️ Апетит та травлення",
            "pl": "🍽️ Apetyt i trawienie",
            "en": "🍽️ Appetite and digestion",
        },
        "short": False,
        "question": {
            "ua": "Яку їжу ви найбільше любите?",
            "pl": "Jakie jedzenie najbardziej lubisz?",
            "en": "What food do you like most?",
        },
        "options": {
            "vata": {
                "ua": "Тепле, вологе, солодке, солоне або кисле",
                "pl": "Ciepłe, wilgotne, słodkie, słone lub kwaśne",
                "en": "Warm, moist, sweet, salty or sour",
            },
            "pitta": {
                "ua": "Холодне, солодке, гірке або терпке",
                "pl": "Zimne, słodkie, gorzkie lub cierpkie",
                "en": "Cool, sweet, bitter or astringent",
            },
            "kapha": {
                "ua": "Гостре, гірке, терпке, легка їжа",
                "pl": "Ostre, gorzkie, cierpkie, lekkie potrawy",
                "en": "Spicy, bitter, astringent, light food",
            },
        },
    },

    # ── БЛОК 5: СОН (питання 13-15) ───────────────────────
    {
        "id": 13,
        "category": "sleep",
        "category_name": {
            "ua": "😴 Сон",
            "pl": "😴 Sen",
            "en": "😴 Sleep",
        },
        "short": True,
        "question": {
            "ua": "Яка у вас якість сну?",
            "pl": "Jaka jest jakość Twojego snu?",
            "en": "What is the quality of your sleep?",
        },
        "options": {
            "vata": {
                "ua": "Поганий, переривчастий, часто прокидаюсь",
                "pl": "Zły, przerywany, często się budzę",
                "en": "Poor, interrupted, wake up often",
            },
            "pitta": {
                "ua": "Середній, легко прокидаюсь, буває безсоння",
                "pl": "Średni, łatwo się budzę, zdarza się bezsenność",
                "en": "Medium, wake up easily, sometimes insomnia",
            },
            "kapha": {
                "ua": "Глибокий і довгий, важко прокидатись",
                "pl": "Głęboki i długi, trudno się obudzić",
                "en": "Deep and long, hard to wake up",
            },
        },
    },

    {
        "id": 14,
        "category": "sleep",
        "category_name": {
            "ua": "😴 Сон",
            "pl": "😴 Sen",
            "en": "😴 Sleep",
        },
        "short": False,
        "question": {
            "ua": "Скільки годин сну вам потрібно?",
            "pl": "Ile godzin snu potrzebujesz?",
            "en": "How many hours of sleep do you need?",
        },
        "options": {
            "vata": {
                "ua": "Менше 6-7 годин, але відчуваю втому",
                "pl": "Mniej niż 6-7 godzin, ale czuję zmęczenie",
                "en": "Less than 6-7 hours but feel tired",
            },
            "pitta": {
                "ua": "6-8 годин, прокидаюсь бадьорим",
                "pl": "6-8 godzin, budzę się wypoczęty",
                "en": "6-8 hours, wake up refreshed",
            },
            "kapha": {
                "ua": "Більше 8-9 годин, вранці важко встати",
                "pl": "Ponad 8-9 godzin, rano trudno wstać",
                "en": "More than 8-9 hours, hard to get up in morning",
            },
        },
    },

    {
        "id": 15,
        "category": "sleep",
        "category_name": {
            "ua": "😴 Сон",
            "pl": "😴 Sen",
            "en": "😴 Sleep",
        },
        "short": False,
        "question": {
            "ua": "Які у вас сни?",
            "pl": "Jakie masz sny?",
            "en": "What are your dreams like?",
        },
        "options": {
            "vata": {
                "ua": "Часті, яскраві, тривожні, про польоти або погоню",
                "pl": "Częste, żywe, niespokojne, o lataniu lub pościgu",
                "en": "Frequent, vivid, anxious, about flying or chasing",
            },
            "pitta": {
                "ua": "Інтенсивні, кольорові, про конфлікти або пригоди",
                "pl": "Intensywne, kolorowe, o konfliktach lub przygodach",
                "en": "Intense, colorful, about conflicts or adventures",
            },
            "kapha": {
                "ua": "Рідкі, спокійні, про воду, природу або їжу",
                "pl": "Rzadkie, spokojne, o wodzie, naturze lub jedzeniu",
                "en": "Rare, calm, about water, nature or food",
            },
        },
    },

    # ── БЛОК 6: ЕНЕРГІЯ (питання 16-18) ───────────────────
    {
        "id": 16,
        "category": "energy",
        "category_name": {
            "ua": "⚡ Енергія",
            "pl": "⚡ Energia",
            "en": "⚡ Energy",
        },
        "short": True,
        "question": {
            "ua": "Який у вас рівень енергії протягом дня?",
            "pl": "Jaki jest Twój poziom energii w ciągu dnia?",
            "en": "What is your energy level throughout the day?",
        },
        "options": {
            "vata": {
                "ua": "Нестабільний, різкі підйоми і спади",
                "pl": "Niestabilny, gwałtowne wzloty i upadki",
                "en": "Unstable, sudden bursts and crashes",
            },
            "pitta": {
                "ua": "Стабільний і сильний, цілеспрямований",
                "pl": "Stabilny i silny, ukierunkowany",
                "en": "Stable and strong, focused",
            },
            "kapha": {
                "ua": "Рівний але низький, потрібна мотивація",
                "pl": "Równy ale niski, potrzebna motywacja",
                "en": "Even but low, need motivation to start",
            },
        },
    },

    {
        "id": 17,
        "category": "energy",
        "category_name": {
            "ua": "⚡ Енергія",
            "pl": "⚡ Energia",
            "en": "⚡ Energy",
        },
        "short": False,
        "question": {
            "ua": "Як ви реагуєте на фізичне навантаження?",
            "pl": "Jak reagujesz na wysiłek fizyczny?",
            "en": "How do you respond to physical exercise?",
        },
        "options": {
            "vata": {
                "ua": "Швидко втомлююсь, потрібен відпочинок",
                "pl": "Szybko się męczę, potrzebuję odpoczynku",
                "en": "Tire quickly, need frequent rest",
            },
            "pitta": {
                "ua": "Люблю інтенсивні тренування, є витривалість",
                "pl": "Lubię intensywne treningi, mam wytrzymałość",
                "en": "Love intense workouts, have good endurance",
            },
            "kapha": {
                "ua": "Повільний старт але добра витривалість",
                "pl": "Wolny start ale dobra wytrzymałość",
                "en": "Slow to start but good endurance",
            },
        },
    },

    {
        "id": 18,
        "category": "energy",
        "category_name": {
            "ua": "⚡ Енергія",
            "pl": "⚡ Energia",
            "en": "⚡ Energy",
        },
        "short": False,
        "question": {
            "ua": "Як ви почуваєтесь вранці?",
            "pl": "Jak się czujesz rano?",
            "en": "How do you feel in the morning?",
        },
        "options": {
            "vata": {
                "ua": "По-різному, часто тривожно або розсіяно",
                "pl": "Różnie, często niespokojnie lub roztargniony",
                "en": "Variable, often anxious or scattered",
            },
            "pitta": {
                "ua": "Бадьоро і готовий до дій",
                "pl": "Rześko i gotowy do działania",
                "en": "Alert and ready for action",
            },
            "kapha": {
                "ua": "Сонливо, потрібен час щоб розігрітись",
                "pl": "Sennie, potrzebuję czasu żeby się rozruszać",
                "en": "Sleepy, need time to warm up",
            },
        },
    },

    # ── БЛОК 7: МИСЛЕННЯ (питання 19-21) ──────────────────
    {
        "id": 19,
        "category": "mind",
        "category_name": {
            "ua": "🧠 Мислення та мова",
            "pl": "🧠 Myślenie i mowa",
            "en": "🧠 Thinking and speech",
        },
        "short": True,
        "question": {
            "ua": "Як ви говорите?",
            "pl": "Jak mówisz?",
            "en": "How do you speak?",
        },
        "options": {
            "vata": {
                "ua": "Швидко, багато, перестрибую з теми на тему",
                "pl": "Szybko, dużo, przeskakuję z tematu na temat",
                "en": "Fast, a lot, jump from topic to topic",
            },
            "pitta": {
                "ua": "Чітко, переконливо, люблю дискутувати",
                "pl": "Wyraźnie, przekonująco, lubię dyskutować",
                "en": "Clear, convincing, love to debate",
            },
            "kapha": {
                "ua": "Повільно, спокійно, обдумую перш ніж говорити",
                "pl": "Powoli, spokojnie, przemyśluję zanim powiem",
                "en": "Slowly, calmly, think before speaking",
            },
        },
    },

    {
        "id": 20,
        "category": "mind",
        "category_name": {
            "ua": "🧠 Мислення та мова",
            "pl": "🧠 Myślenie i mowa",
            "en": "🧠 Thinking and speech",
        },
        "short": False,
        "question": {
            "ua": "Як ви приймаєте рішення?",
            "pl": "Jak podejmujesz decyzje?",
            "en": "How do you make decisions?",
        },
        "options": {
            "vata": {
                "ua": "Імпульсивно, часто змінюю рішення",
                "pl": "Impulsywnie, często zmieniam decyzje",
                "en": "Impulsively, often change my mind",
            },
            "pitta": {
                "ua": "Швидко і впевнено, аналізую факти",
                "pl": "Szybko i pewnie, analizuję fakty",
                "en": "Quickly and confidently, analyze facts",
            },
            "kapha": {
                "ua": "Повільно але надійно, рідко змінюю рішення",
                "pl": "Powoli ale niezawodnie, rzadko zmieniam decyzje",
                "en": "Slowly but reliably, rarely change decisions",
            },
        },
    },

    {
        "id": 21,
        "category": "mind",
        "category_name": {
            "ua": "🧠 Мислення та мова",
            "pl": "🧠 Myślenie i mowa",
            "en": "🧠 Thinking and speech",
        },
        "short": False,
        "question": {
            "ua": "Як ви реагуєте на зміни?",
            "pl": "Jak reagujesz na zmiany?",
            "en": "How do you react to change?",
        },
        "options": {
            "vata": {
                "ua": "Люблю зміни, але вони мене виснажують",
                "pl": "Lubię zmiany, ale mnie wyczerpują",
                "en": "Love change but it exhausts me",
            },
            "pitta": {
                "ua": "Адаптуюсь швидко, беру контроль",
                "pl": "Adaptuję się szybko, przejmuję kontrolę",
                "en": "Adapt quickly, take control",
            },
            "kapha": {
                "ua": "Не люблю зміни, надаю перевагу стабільності",
                "pl": "Nie lubię zmian, preferuję stabilność",
                "en": "Dislike change, prefer stability",
            },
        },
    },

    # ── БЛОК 8: ПАМ'ЯТЬ (питання 22-24) ──────────────────
    {
        "id": 22,
        "category": "memory",
        "category_name": {
            "ua": "💭 Пам'ять та навчання",
            "pl": "💭 Pamięć i nauka",
            "en": "💭 Memory and learning",
        },
        "short": True,
        "question": {
            "ua": "Як ви навчаєтесь новому?",
            "pl": "Jak się uczysz nowych rzeczy?",
            "en": "How do you learn new things?",
        },
        "options": {
            "vata": {
                "ua": "Швидко схоплюю але швидко забуваю",
                "pl": "Szybko łapię ale szybko zapominam",
                "en": "Grasp quickly but forget quickly",
            },
            "pitta": {
                "ua": "Швидко вчуся і добре пам'ятаю деталі",
                "pl": "Szybko się uczę i dobrze pamiętam szczegóły",
                "en": "Learn fast and remember details well",
            },
            "kapha": {
                "ua": "Повільно вчуся але пам'ятаю надовго",
                "pl": "Uczę się powoli ale pamiętam długo",
                "en": "Learn slowly but remember for a long time",
            },
        },
    },

    {
        "id": 23,
        "category": "memory",
        "category_name": {
            "ua": "💭 Пам'ять та навчання",
            "pl": "💭 Pamięć i nauka",
            "en": "💭 Memory and learning",
        },
        "short": False,
        "question": {
            "ua": "Яка у вас довготривала пам'ять?",
            "pl": "Jaka jest Twoja pamięć długotrwała?",
            "en": "How is your long-term memory?",
        },
        "options": {
            "vata": {
                "ua": "Слабка, забуваю імена та деталі",
                "pl": "Słaba, zapominam imiona i szczegóły",
                "en": "Weak, forget names and details",
            },
            "pitta": {
                "ua": "Гарна, пам'ятаю факти і деталі",
                "pl": "Dobra, pamiętam fakty i szczegóły",
                "en": "Good, remember facts and details",
            },
            "kapha": {
                "ua": "Відмінна, пам'ятаю все що вивчив",
                "pl": "Doskonała, pamiętam wszystko czego się nauczyłem",
                "en": "Excellent, remember everything I learned",
            },
        },
    },

    {
        "id": 24,
        "category": "memory",
        "category_name": {
            "ua": "💭 Пам'ять та навчання",
            "pl": "💭 Pamięć i nauka",
            "en": "💭 Memory and learning",
        },
        "short": False,
        "question": {
            "ua": "Як ви концентруєтесь?",
            "pl": "Jak się koncentrujesz?",
            "en": "How do you concentrate?",
        },
        "options": {
            "vata": {
                "ua": "Важко, думки розсіюються, потрібна тиша",
                "pl": "Trudno, myśli się rozpraszają, potrzebuję ciszy",
                "en": "Difficult, thoughts scatter, need silence",
            },
            "pitta": {
                "ua": "Добре, можу зосередитись на деталях",
                "pl": "Dobrze, mogę skupić się na szczegółach",
                "en": "Well, can focus on details",
            },
            "kapha": {
                "ua": "Добре але повільно, потрібен час на розгін",
                "pl": "Dobrze ale powoli, potrzebuję czasu na rozruch",
                "en": "Well but slowly, need time to get started",
            },
        },
    },

    # ── БЛОК 9: ЕМОЦІЇ (питання 25-27) ────────────────────
    {
        "id": 25,
        "category": "emotions",
        "category_name": {
            "ua": "❤️ Емоції та стрес",
            "pl": "❤️ Emocje i stres",
            "en": "❤️ Emotions and stress",
        },
        "short": True,
        "question": {
            "ua": "Як ви реагуєте на стрес?",
            "pl": "Jak reagujesz na stres?",
            "en": "How do you react to stress?",
        },
        "options": {
            "vata": {
                "ua": "Тривога, страх, паніка, нервозність",
                "pl": "Niepokój, strach, panika, nerwowość",
                "en": "Anxiety, fear, panic, nervousness",
            },
            "pitta": {
                "ua": "Роздратування, гнів, критика, нетерпіння",
                "pl": "Irytacja, gniew, krytyka, niecierpliwość",
                "en": "Irritation, anger, criticism, impatience",
            },
            "kapha": {
                "ua": "Замикаюсь, уникаю конфліктів, накопичую образи",
                "pl": "Zamykam się, unikam konfliktów, kumuluję urazy",
                "en": "Withdraw, avoid conflicts, accumulate grievances",
            },
        },
    },

    {
        "id": 26,
        "category": "emotions",
        "category_name": {
            "ua": "❤️ Емоції та стрес",
            "pl": "❤️ Emocje i stres",
            "en": "❤️ Emotions and stress",
        },
        "short": False,
        "question": {
            "ua": "Яка ваша переважна емоція?",
            "pl": "Jaka jest Twoja dominująca emocja?",
            "en": "What is your predominant emotion?",
        },
        "options": {
            "vata": {
                "ua": "Тривога і занепокоєння — autsukya",
                "pl": "Niepokój i zamartwianie się — autsukya",
                "en": "Anxiety and worry — autsukya",
            },
            "pitta": {
                "ua": "Гнів і роздратування — moha",
                "pl": "Gniew i irytacja — moha",
                "en": "Anger and irritation — moha",
            },
            "kapha": {
                "ua": "Смуток і депресія — arati",
                "pl": "Smutek i depresja — arati",
                "en": "Sadness and depression — arati",
            },
        },
    },

    {
        "id": 27,
        "category": "emotions",
        "category_name": {
            "ua": "❤️ Емоції та стрес",
            "pl": "❤️ Emocje i stres",
            "en": "❤️ Emotions and stress",
        },
        "short": False,
        "question": {
            "ua": "Який ваш улюблений клімат?",
            "pl": "Jaki jest Twój ulubiony klimat?",
            "en": "What is your favorite climate?",
        },
        "options": {
            "vata": {
                "ua": "Тепло і вологість, не люблю вітер і холод",
                "pl": "Ciepło i wilgotność, nie lubię wiatru i zimna",
                "en": "Warm and humid, dislike wind and cold",
            },
            "pitta": {
                "ua": "Прохолода, не люблю спеку і вологість",
                "pl": "Chłód, nie lubię upału i wilgotności",
                "en": "Cool weather, dislike heat and humidity",
            },
            "kapha": {
                "ua": "Тепло і сухість, не люблю холод і вологість",
                "pl": "Ciepło i suchość, nie lubię zimna i wilgotności",
                "en": "Warm and dry, dislike cold and dampness",
            },
        },
    },
]

SHORT_QUESTIONS = [q for q in PRAKRITI_QUESTIONS if q["short"]]


# =============================================================
# ТЕСТ ВІКРІТІ
# Вікріті — поточний стан, може відрізнятись від Пракріті
# Інструкція: "Як ви почуваєтесь ЗАРАЗ, останні 2-4 тижні"
# =============================================================

VIKRITI_QUESTIONS = [
  {
    "id": 1,
    "question": {
      "ua": "Як працює ваше травлення останнім часом?",
      "pl": "Jak działa Twoje trawienie ostatnio?",
      "en": "How has your digestion been working lately?"
    },
    "options": {
      "vata": {
        "ua": "Нерегулярно — то нормально, то здуття і гази, апетит непостійний",
        "pl": "Nieregularnie — raz dobrze, raz wzdęcia i gazy, apetyt zmienny",
        "en": "Irregular — sometimes fine, sometimes bloating and gas, appetite fluctuates"
      },
      "pitta": {
        "ua": "Сильне і швидке — постійно хочу їсти, дратуюсь якщо пропускаю прийом їжі",
        "pl": "Silne i szybkie — ciągle chcę jeść, irytuję się gdy opuszczę posiłek",
        "en": "Strong and fast — always hungry, get irritable if I skip a meal"
      },
      "kapha": {
        "ua": "Повільне і стабільне — можу легко пропустити прийом їжі, але після їди буває тяжкість",
        "pl": "Powolne i stabilne — mogę łatwo pominąć posiłek, ale po jedzeniu bywa ciężkość",
        "en": "Slow and steady — can easily skip a meal, but feel heavy after eating"
      }
    }
  },
  {
    "id": 2,
    "question": {
      "ua": "Як ви зазвичай спите?",
      "pl": "Jak zwykle sypiasz?",
      "en": "How do you usually sleep?"
    },
    "options": {
      "vata": {
        "ua": "Сон легкий і переривчастий — часто прокидаюсь, думки не дають заснути",
        "pl": "Sen lekki i przerywany — często się budzę, myśli nie dają zasnąć",
        "en": "Light and interrupted — I often wake up, thoughts keep me from falling asleep"
      },
      "pitta": {
        "ua": "Засинаю нормально, але іноді прокидаюсь серед ночі від жару або неспокійних снів",
        "pl": "Zasypiam normalnie, ale czasem budzę się w nocy z gorąca lub niespokojnych snów",
        "en": "I fall asleep fine, but sometimes wake up at night from heat or intense dreams"
      },
      "kapha": {
        "ua": "Сплю глибоко і довго — важко прокинутись, вранці відчуваю млявість",
        "pl": "Śpię głęboko i długo — trudno się obudzić, rano czuję ospałość",
        "en": "I sleep deeply and long — hard to wake up, feel sluggish in the morning"
      }
    }
  },
  {
    "id": 3,
    "question": {
      "ua": "Який стан вашої шкіри зараз?",
      "pl": "Jaki jest stan Twojej skóry teraz?",
      "en": "What is the condition of your skin right now?"
    },
    "options": {
      "vata": {
        "ua": "Суха, іноді лущиться, схильна до шорсткості, особливо на руках і ногах",
        "pl": "Sucha, czasem się łuszczy, szorstka, szczególnie na rękach i nogach",
        "en": "Dry, sometimes flaky, tends to be rough, especially on hands and feet"
      },
      "pitta": {
        "ua": "Тепла, чутлива, схильна до почервонінь або висипів, іноді жирна в Т-зоні",
        "pl": "Ciepła, wrażliwa, skłonna do zaczerwienień lub wysypek, czasem tłusta w strefie T",
        "en": "Warm, sensitive, prone to redness or rashes, sometimes oily in the T-zone"
      },
      "kapha": {
        "ua": "М'яка і зволожена, але схильна до жирності, розширених пор, іноді набряклість",
        "pl": "Miękka i nawilżona, ale skłonna do tłustości, rozszerzonych porów, czasem opuchlizna",
        "en": "Soft and moisturized, but tends to be oily, with enlarged pores, sometimes puffy"
      }
    }
  },
  {
    "id": 4,
    "question": {
      "ua": "Ваша реакція на холод і вітер:",
      "pl": "Twoja reakcja na zimno i wiatr:",
      "en": "Your reaction to cold and wind:"
    },
    "options": {
      "vata": {
        "ua": "Мерзну швидко, з'являється сухість шкіри і внутрішній неспокій",
        "pl": "Szybko marznę, pojawia się suchość skóry i wewnętrzny niepokój",
        "en": "I get cold quickly, skin becomes dry and I feel inner restlessness"
      },
      "pitta": {
        "ua": "Переношу добре, навіть приємно прохолодитись, але дратує сильний вітер",
        "pl": "Znoszę dobrze, nawet lubię ochłodę, ale denerwuje silny wiatr",
        "en": "I handle it well, even enjoy cooling down, but strong wind is annoying"
      },
      "kapha": {
        "ua": "Переношу нормально, але в сиру холодну погоду з'являється закладеність носа і млявість",
        "pl": "Znoszę normalnie, ale w wilgotną zimną pogodę pojawia się zatkany nos i ospałość",
        "en": "I handle it okay, but in damp cold weather I get congestion and sluggishness"
      }
    }
  },
  {
    "id": 5,
    "question": {
      "ua": "Як ви реагуєте на стресову ситуацію?",
      "pl": "Jak reagujesz na sytuację stresową?",
      "en": "How do you react to a stressful situation?"
    },
    "options": {
      "vata": {
        "ua": "Тривожусь, хвилююсь, думки скачуть, важко зосередитись",
        "pl": "Niepokoję się, zamartiam, myśli skaczą, trudno się skupić",
        "en": "I get anxious, worry a lot, racing thoughts, hard to focus"
      },
      "pitta": {
        "ua": "Дратуюсь, злюсь, хочу все контролювати і виправити негайно",
        "pl": "Irytuję się, złoszczę, chcę wszystko kontrolować i natychmiast naprawić",
        "en": "I get irritated, angry, want to control everything and fix it immediately"
      },
      "kapha": {
        "ua": "Замикаюсь в собі, уникаю конфлікту, можу заїдати стрес або впадати в апатію",
        "pl": "Zamykam się w sobie, unikam konfliktu, mogę zajadać stres lub wpadać w apatię",
        "en": "I withdraw, avoid conflict, may comfort-eat or fall into apathy"
      }
    }
  },
  {
    "id": 6,
    "question": {
      "ua": "Який у вас рівень енергії протягом дня?",
      "pl": "Jaki masz poziom energii w ciągu dnia?",
      "en": "What is your energy level throughout the day?"
    },
    "options": {
      "vata": {
        "ua": "Хвилями — то раптовий сплеск активності, то різкий спад і втома",
        "pl": "Falami — raz nagły przypływ aktywności, raz gwałtowny spadek i zmęczenie",
        "en": "In waves — sudden bursts of activity, then sharp drops and fatigue"
      },
      "pitta": {
        "ua": "Висока і стабільна до середини дня, потім можу перегоріти якщо не відпочину",
        "pl": "Wysoka i stabilna do połowy dnia, potem mogę się wypalić jeśli nie odpocznę",
        "en": "High and steady until midday, then I may burn out if I don't rest"
      },
      "kapha": {
        "ua": "Розкачуюсь повільно, але тримаю стабільний рівень; зранку і після їди — млявість",
        "pl": "Rozkręcam się powoli, ale utrzymuję stabilny poziom; rano i po jedzeniu — ospałość",
        "en": "I warm up slowly but stay steady; mornings and after meals I feel sluggish"
      }
    }
  },
  {
    "id": 7,
    "question": {
      "ua": "Як працює ваш кишечник (випорожнення)?",
      "pl": "Jak działa Twój jelito (wypróżnianie)?",
      "en": "How are your bowel movements?"
    },
    "options": {
      "vata": {
        "ua": "Нерегулярно — схильність до затримок, сухий або твердий стул",
        "pl": "Nieregularnie — skłonność do zaparć, suchy lub twardy stolec",
        "en": "Irregular — tendency towards constipation, dry or hard stool"
      },
      "pitta": {
        "ua": "Регулярно, іноді занадто часто — стул м'який, буває печіння або рідкий",
        "pl": "Regularnie, czasem za często — stolec miękki, bywa pieczenie lub luźny",
        "en": "Regular, sometimes too frequent — soft stool, occasional burning or loose"
      },
      "kapha": {
        "ua": "Регулярно але повільно — стул важкий, об'ємний, іноді з відчуттям неповного спорожнення",
        "pl": "Regularnie ale powoli — stolec ciężki, obfity, czasem z uczuciem niepełnego wypróżnienia",
        "en": "Regular but slow — stool heavy, bulky, sometimes with a feeling of incomplete evacuation"
      }
    }
  },
  {
    "id": 8,
    "question": {
      "ua": "Опишіть ваш розумовий стан останнім часом:",
      "pl": "Opisz swój stan umysłowy ostatnio:",
      "en": "Describe your mental state lately:"
    },
    "options": {
      "vata": {
        "ua": "Розум неспокійний, багато ідей одночасно, важко довести справу до кінця",
        "pl": "Umysł niespokojny, wiele pomysłów naraz, trudno doprowadzić sprawę do końca",
        "en": "Restless mind, many ideas at once, hard to follow through on things"
      },
      "pitta": {
        "ua": "Гострий і критичний — аналізую все, схильний до перфекціонізму і нетерпимості",
        "pl": "Ostry i krytyczny — analizuję wszystko, skłonny do perfekcjonizmu i niecierpliwości",
        "en": "Sharp and critical — I analyze everything, prone to perfectionism and impatience"
      },
      "kapha": {
        "ua": "Спокійний, але важко починати нове — схильність до відкладання і ментальної інерції",
        "pl": "Spokojny, ale trudno zacząć coś nowego — skłonność do odkładania i mentalnej inercji",
        "en": "Calm, but hard to start new things — tendency to procrastinate and mental inertia"
      }
    }
  },
  {
    "id": 9,
    "question": {
      "ua": "Як змінюється ваша вага?",
      "pl": "Jak zmienia się Twoja waga?",
      "en": "How does your weight change?"
    },
    "options": {
      "vata": {
        "ua": "Важко набрати вагу — швидко худну від стресу або нерегулярного харчування",
        "pl": "Trudno przybrać na wadze — szybko chudnę od stresu lub nieregularnego jedzenia",
        "en": "Hard to gain weight — I lose weight quickly from stress or irregular eating"
      },
      "pitta": {
        "ua": "Вага стабільна поки контролюю харчування, набираю і скидаю відносно легко",
        "pl": "Waga stabilna dopóki kontroluję jedzenie, przybieram i zrzucam stosunkowo łatwo",
        "en": "Weight is stable as long as I watch my diet, I gain and lose relatively easily"
      },
      "kapha": {
        "ua": "Легко набираю вагу і дуже важко скидаю, навіть при обмеженні їжі",
        "pl": "Łatwo przybieram na wadze i bardzo trudno zrzucam, nawet przy ograniczeniu jedzenia",
        "en": "I gain weight easily and find it very hard to lose, even when restricting food"
      }
    }
  },
  {
    "id": 10,
    "question": {
      "ua": "Як ваш організм зазвичай реагує на зміну сезону або погоди?",
      "pl": "Jak Twój organizm zwykle reaguje na zmianę pory roku lub pogody?",
      "en": "How does your body usually react to seasonal or weather changes?"
    },
    "options": {
      "vata": {
        "ua": "Восени і при вітрі — сухість шкіри, тріскаються губи, неспокій, ломота в суглобах",
        "pl": "Jesienią i przy wietrze — suchość skóry, pękające usta, niepokój, bóle stawów",
        "en": "In autumn and wind — dry skin, cracked lips, restlessness, joint aches"
      },
      "pitta": {
        "ua": "Влітку і в спеку — шкіра червоніє, з'являється дратівливість, печія, висипи",
        "pl": "Latem i w upały — skóra się czerwieni, pojawia się drażliwość, zgaga, wysypki",
        "en": "In summer and heat — skin gets red, irritability, heartburn, rashes appear"
      },
      "kapha": {
        "ua": "Навесні і в сиру погоду — закладеність носа, набряклість, втома, небажання рухатись",
        "pl": "Wiosną i w wilgotną pogodę — zatkany nos, obrzęki, zmęczenie, niechęć do ruchu",
        "en": "In spring and damp weather — nasal congestion, puffiness, fatigue, reluctance to move"
      }
    }
  }
]