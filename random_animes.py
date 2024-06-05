from random import choice
import webbrowser

# create dictionary of genres and their corresponding anime titles and Crunchyroll URLs
anime_dict = {
    'Action': [
        {'title': 'Naruto', 'url': 'https://www.crunchyroll.com/naruto'},
        {'title': 'Bleach', 'url': 'https://www.crunchyroll.com/bleach'},
        {'title': 'One Piece', 'url': 'https://www.crunchyroll.com/one-piece'},
        {'title': 'Attack on Titan', 'url': 'https://www.crunchyroll.com/attack-on-titan'},
        {'title': 'Fullmetal Alchemist: Brotherhood', 'url': 'https://www.crunchyroll.com/fullmetal-alchemist-brotherhood'},
        {'title': 'My Hero Academia', 'url': 'https://www.crunchyroll.com/my-hero-academia'},
        {'title': 'Demon Slayer: Kimetsu no Yaiba', 'url': 'https://www.crunchyroll.com/demon-slayer-kimetsu-no-yaiba'},
        {'title': 'Jujutsu Kaisen', 'url': 'https://www.crunchyroll.com/jujutsu-kaisen'},
        {'title': 'Black Clover', 'url': 'https://www.crunchyroll.com/black-clover'},
        {'title': 'Sword Art Online', 'url': 'https://www.crunchyroll.com/sword-art-online'}
    ],
    'Fantasy': [
        {'title': 'Mushishi', 'url': 'https://www.crunchyroll.com/mushishi'},
        {'title': 'The Ancient Magus\' Bride', 'url': 'https://www.crunchyroll.com/the-ancient-magus-bride'},
        {'title': 'Re:Zero -Starting Life in Another World-', 'url': 'https://www.crunchyroll.com/rezero-starting-life-in-another-world-'},
        {'title': 'Overlord', 'url': 'https://www.crunchyroll.com/overlord'},
        {'title': 'KonoSuba: God\'s Blessing on This Wonderful World!', 'url': 'https://www.crunchyroll.com/konosuba-gods-blessing-on-this-wonderful-world'},
        {'title': 'That Time I Got Reincarnated as a Slime', 'url': 'https://www.crunchyroll.com/that-time-i-got-reincarnated-as-a-slime'},
        {'title': 'The Rising of the Shield Hero', 'url': 'https://www.crunchyroll.com/the-rising-of-the-shield-hero'},
        {'title': 'No Game No Life', 'url': 'https://www.crunchyroll.com/no-game-no-life'},
        {'title': 'Log Horizon', 'url': 'https://www.crunchyroll.com/log-horizon'},
        {'title': 'Goblin Slayer', 'url': 'https://www.crunchyroll.com/goblin-slayer'}
    ],
    'Romance': [
        {'title': 'Your Lie in April', 'url': 'https://www.crunchyroll.com/your-lie-in-april'},
        {'title': 'Toradora!', 'url': 'https://www.crunchyroll.com/toradora'},
        {'title': 'Kaguya-sama: Love is War', 'url': 'https://www.crunchyroll.com/kaguya-sama-love-is-war'},
        {'title': 'Horimiya', 'url': 'https://www.crunchyroll.com/horimiya'},
        {'title': 'Fruits Basket', 'url': 'https://www.crunchyroll.com/fruits-basket'},
        {'title': 'Rascal Does Not Dream of Bunny Girl Senpai', 'url': 'https://www.crunchyroll.com/rascal-does-not-dream-of-bunny-girl-senpai'},
        {'title': 'My Love Story!!', 'url': 'https://www.crunchyroll.com/my-love-story'},
        {'title': 'Maid Sama!', 'url': 'https://www.crunchyroll.com/maid-sama'},
        {'title': 'Snow White with the Red Hair', 'url': 'https://www.crunchyroll.com/snow-white-with-the-red-hair'},
        {'title': 'Ao Haru Ride', 'url': 'https://www.crunchyroll.com/ao-haru-ride'}
    ],
    'Sci-Fi': [
        {'title': 'Steins;Gate', 'url': 'https://www.crunchyroll.com/steinsgate'},
        {'title': 'Psycho-Pass', 'url': 'https://www.crunchyroll.com/psycho-pass'},
        {'title': 'Cowboy Bebop', 'url': 'https://www.crunchyroll.com/cowboy-bebop'},
        {'title': 'Neon Genesis Evangelion', 'url': 'https://www.netflix.com/title/81033445'},
        {'title': 'Code Geass: Lelouch of the Rebellion', 'url': 'https://www.crunchyroll.com/code-geass'},
        {'title': 'Ghost in the Shell: Stand Alone Complex', 'url': 'https://www.crunchyroll.com/ghost-in-the-shell-stand-alone-complex'},
        {'title': 'Ergo Proxy', 'url': 'https://www.crunchyroll.com/ergo-proxy'},
        {'title': 'Psycho-Pass 2', 'url': 'https://www.crunchyroll.com/psycho-pass'},
        {'title': 'Gundam Wing', 'url': 'https://www.crunchyroll.com/mobile-suit-gundam-wing'},
        {'title': 'Darling in the Franxx', 'url': 'https://www.crunchyroll.com/darling-in-the-franxx'}
    ],
    'Sports': [
        {'title': 'Haikyuu!!', 'url': 'https://www.crunchyroll.com/haikyu'},
        {'title': 'Kuroko\'s Basketball', 'url': 'https://www.crunchyroll.com/kurokos-basketball'},
        {'title': 'Free!', 'url': 'https://www.crunchyroll.com/free-iwatobi-swim-club'},
        {'title': 'Yuri!!! on Ice', 'url': 'https://www.crunchyroll.com/yuri-on-ice'},
        {'title': 'Ace of Diamond', 'url': 'https://www.crunchyroll.com/ace-of-the-diamond'},
        {'title': 'Eyeshield 21', 'url': 'https://www.crunchyroll.com/eyeshield-21'},
        {'title': 'Big Windup!', 'url': 'https://www.crunchyroll.com/big-windup'},
        {'title': 'Chihayafuru', 'url': 'https://www.crunchyroll.com/chihayafuru'},
        {'title': 'Yowamushi Pedal', 'url': 'https://www.crunchyroll.com/yowamushi-pedal'},
        {'title': 'Prince of Stride: Alternative', 'url': 'https://www.crunchyroll.com/prince-of-stride-alternative'}
    ],
    'Thriller': [
        {'title': 'Death Note', 'url': 'https://www.crunchyroll.com/death-note'},
        {'title': 'Monster', 'url': 'https://www.youtube.com/watch?v=msTB5r8nUHU&list=PL3ZHtfY1VuEdSJkLQfQTBhEO79RjjIsLt'},
        {'title': 'Erased', 'url': 'https://www.crunchyroll.com/erased'},
        {'title': 'The Promised Neverland', 'url': 'https://www.crunchyroll.com/the-promised-neverland'},
        {'title': 'Mirai Nikki', 'url': 'https://www.crunchyroll.com/the-future-diary'},
        {'title': 'Parasyte -the maxim-', 'url': 'https://www.crunchyroll.com/parasyte-the-maxim-'},
        {'title': 'Tokyo Ghoul', 'url': 'https://www.crunchyroll.com/tokyo-ghoul'},
        {'title': 'Higurashi: When They Cry', 'url': 'https://www.crunchyroll.com/when-they-cry'},
        {'title': 'Terror in Resonance', 'url': 'https://www.crunchyroll.com/terror-in-resonance'},
        {'title': 'Psycho-Pass: The Movie', 'url': 'https://www.crunchyroll.com/psycho-pass-the-movie'}
    ],
    'Comedy': [
        {'title': 'Gintama', 'url': 'https://www.crunchyroll.com/gintama'},
        {'title': 'KonoSuba: God\'s Blessing on this Wonderful World!', 'url': 'https://www.crunchyroll.com/konosuba-gods-blessing-on-this-wonderful-world'},
        {'title': 'One Punch Man', 'url': 'https://www.crunchyroll.com/one-punch-man'},
        {'title': 'Mob Psycho 100', 'url': 'https://www.crunchyroll.com/mob-psycho-100'},
        {'title': 'The Disastrous Life of Saiki K.', 'url': 'https://www.crunchyroll.com/the-disastrous-life-of-saiki-k'},
        {'title': 'Nichijou - My Ordinary Life', 'url': 'https://www.crunchyroll.com/nichijou-my-ordinary-life'},
        {'title': 'The Devil is a Part-Timer!', 'url': 'https://www.crunchyroll.com/the-devil-is-a-part-timer'},
        {'title': 'Monthly Girls\' Nozaki-kun', 'url': 'https://www.crunchyroll.com/monthly-girls-nozaki-kun'},
        {'title': 'Hinamatsuri', 'url': 'https://www.crunchyroll.com/hinamatsuri'},
        {'title': 'Asobi Asobase - workshop of fun -', 'url': 'https://www.crunchyroll.com/asobi-asobase-workshop-of-fun-'}
    ],
    'Mystery': [
        {'title': 'Durarara!!', 'url': 'https://www.crunchyroll.com/durarara'},
        {'title': 'Baccano!', 'url': 'https://www.crunchyroll.com/baccano'},
        {'title': 'Gosick', 'url': 'https://www.crunchyroll.com/gosick'},
        {'title': 'Hyouka', 'url': 'https://www.crunchyroll.com/hyouka'},
        {'title': 'Occultic;Nine', 'url': 'https://www.crunchyroll.com/occulticnine'},
        {'title': 'Rokka -Braves of the Six Flowers-', 'url': 'https://www.crunchyroll.com/rokka-braves-of-the-six-flowers-'},
        {'title': 'Rampo Kitan: Game of Laplace', 'url': 'https://www.crunchyroll.com/rampo-kitan-game-of-laplace'},
        {'title': 'Un-Go', 'url': 'https://www.crunchyroll.com/un-go'},
        {'title': 'Hakata Tonkotsu Ramens', 'url': 'https://www.crunchyroll.com/hakata-tonkotsu-ramens'},
        {'title': 'Beautiful Bones -Sakurako\'s Investigation-', 'url': 'https://www.crunchyroll.com/Beautiful%20Bones%20Sakurakos%20Investigation'}
    ],
    'Slice of Life': [
        {'title': 'Barakamon', 'url': 'https://www.crunchyroll.com/barakamon'},
        {'title': 'Non Non Biyori', 'url': 'https://www.crunchyroll.com/non-non-biyori'},
        {'title': 'Silver Spoon', 'url': 'https://www.crunchyroll.com/silver-spoon'},
        {'title': 'Usagi Drop', 'url': 'https://www.crunchyroll.com/usagi-drop'},
        {'title': 'Flying Witch', 'url': 'https://www.crunchyroll.com/flying-witch'},
        {'title': 'Poco\'s Udon World', 'url': 'https://www.crunchyroll.com/pocos-udon-world'},
        {'title': 'Hanasaku Iroha', 'url': 'https://www.crunchyroll.com/hanasaku-iroha'},
        {'title': 'Sweetness & Lightning', 'url': 'https://www.crunchyroll.com/sweetness-lightning'},
        {'title': 'Tanaka-kun is Always Listless', 'url': 'https://www.crunchyroll.com/tanaka-kun-is-always-listless'},
        {'title': 'My Roommate is a Cat', 'url': 'https://www.crunchyroll.com/my-roommate-is-a-cat'}
    ]
}

# function to ask for genre preference and select a random anime from that genre
def get_anime_recommendation():
    print("What genre of anime are you in the mood for?")
    for genre in anime_dict:
        print(f"- {genre}")
    
    genre_choice = input("Enter your preferred genre: ")
    
    while genre_choice not in anime_dict:
        genre_choice = input("Invalid genre. Please choose from the available genres: ")
    
    selected_anime = choice(anime_dict[genre_choice])
    print(f"\nYou should watch: {selected_anime['title']}")
    
    depiction_choice = input("Would you like a brief depiction of the selected anime? (yes/no): ")
    if depiction_choice.lower() == 'yes':
        if selected_anime['title'] == 'Naruto':
            print("Naruto is a story about a young ninja who seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village.")
        elif selected_anime['title'] == 'Bleach':
            print("Bleach follows the adventures of Ichigo Kurosaki after he obtains the powers of a Soul Reaper and is forced to defend humans from evil spirits.")
        # Add more depictions for the other anime titles
    
    watch_choice = input("Would you like to watch this anime on Crunchyroll? (yes/no): ")
    if watch_choice.lower() == 'yes':
        webbrowser.open(selected_anime['url'])
    else:
        print("No problem! Feel free to run the program again if you change your mind.")
        
    restart_choice = input("Would you like to get another anime recommendation? (yes/no): ")
    if restart_choice.lower() == 'yes':
        print("\n")
        get_anime_recommendation()
    else:
        print("Thank you for using the Anime Recommendation System. Have a great day!")

# run the anime recommendation function
get_anime_recommendation()