import random



subject_list=[ "Prime Minister",
    "Local chaiwala",
    "Engineering student",
    "Auto driver",
    "Gym trainer",
    "School teacher",
    "Startup founder",
    "YouTuber",
    "Neighbor aunty",
    "Delivery boy",
    "College topper",
    "Hostel roommate",
    "Office employee",
    "Politician",
    "Cricketer",
    "Bollywood actor",
    "Tech support guy",
    "Security guard",
    "Wedding guest",
    "Influencer"]
action_list =[ "dances",
    "launches",
    "announces",
    "declares",
    "bans",
    "orders",
    "cancels",
    "starts",
    "stops",
    "joins",
    "leaves",
    "creates",
    "destroys",
    "forgets",
    "remembers",
    "explains",
    "questions",
    "blames",
    "praises",
    "records",
    "uploads",
    "shares",
    "hides",
    "reveals",
    "discovers",
    "loses",
    "finds",
    "wins",
    "fails",
    "plans",
    "postpones",
    "celebrates",
    "shocks"]
object_list=["at a wedding",
    "during online class",
    "in traffic jam",
    "at railway station",
    "on social media",
    "during IPL match",
    "in exam hall",
    "at tea stall",
    "in gym",
    "during meeting",
    "at midnight",
    "in hostel room",
    "during power cut",
    "at street food stall",
    "in shopping mall",
    "on video call",
    "during rain",
    "in metro",
    "at airport",
    "during festival"]
user =''
        
while True:
    user_choice2=input ("\n do you want to use a specefic name in a headline ?(yes/no) : ").lower().strip()
    
    if user_choice2=='yes':
        user_input=list(input("\n enter names with space: ").split())
        user=random.choice(user_input)
    
    subject=random.choice(subject_list)
    action=random.choice(action_list)
    obj=random.choice (object_list)
    
    if user_choice2=='yes':
            headline = (f"BREAKING: {user}  {action} {obj}")
    else:
        headline = (f"BREAKING: {subject}  {action} {obj}")
    print ("\n" + headline )

    store =input ("\n do you want to store headline in a file ?(yes /no ) : "  ).strip().lower()
    
    if store =="yes":
        
        with open("file.text",'a')as f:
            f.write('\n'+headline)
        fetch =input ( "\n do you want to fetch news from save folder (yes /no) : ").strip().lower()
        
        if fetch =="yes":
            n=int(input ('\n give negetive integer in assending order for previous headline : '))
            with open("file.text",'r')as f:
                 lines =f.readlines()
                 print ('\n'+lines[n])
                 
    users_choice =input('\n do you want to generate another headline? (yes/no) : ').strip().lower()
    
    if users_choice=="no":
        print("\n Thanks for using our platform , have a good day \n ")
        break
                
    
