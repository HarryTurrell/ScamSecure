import random

# Question and answer bank
quiz_data = [
    {
        "question": "You receive a phone call from someone claiming to be from Microsoft. They say your computer has been hacked and ask you to install remote access software so they can “fix it.”",
        "answer": "Computer Software Service Fraud"
    },
    {
        "question": "A stranger offers to help when your card gets stuck in a cash machine. After you leave, they retrieve your card and use the PIN you entered to withdraw money.",
        "answer": "Banking and Card Fraud – Cash Machines"
    },
    {
        "question": "You are contacted by someone on a dating app who quickly declares their love, then says they are stranded overseas and need money for a sick child.",
        "answer": "Romance and Dating Fraud"
    },
    {
        "question": "You get a letter saying you’ve won £10,000 in a prize draw, but to claim it, you must send £30 to cover processing fees.",
        "answer": "Scam Mail"
    },
    {
        "question": "You buy what looks like a discounted luxury holiday villa online. When you arrive, the property doesn’t exist.",
        "answer": "Holiday Fraud"
    },
    {
        "question": "A caller claims to be from your bank and says there’s been fraudulent activity. They urge you to transfer your money to a “safe account.”",
        "answer": "Authorised Push Payment (APP) Fraud"
    },
    {
        "question": "Someone knocks on your door saying your roof is damaged and offers to repair it for £400 cash. After you pay, they leave and never come back.",
        "answer": "Door-to-Door Fraud"
    },
    {
        "question": "You receive an email telling you that you’ve inherited money from a distant relative. To access it, you must first pay a legal release fee.",
        "answer": "Advance Fee Fraud"
    },
    {
        "question": "A company contacts you with an exciting opportunity to invest in a rare gemstone business, promising high returns. You send money and never hear from them again.",
        "answer": "Investment Fraud"
    },
    {
        "question": "You buy a concert ticket from someone on social media. On the day of the event, the ticket turns out to be fake.",
        "answer": "Ticketing Fraud"
    },
    {
        "question": "Your HR department receives an email that appears to be from a senior manager requesting a large payment to a new supplier. After sending it, they realise the email was fake.",
        "answer": "Payment Fraud"
    },
    {
        "question": "Someone calls claiming to be a police officer investigating fraud. You're told to withdraw £2,000 and hand it to a courier for examination.",
        "answer": "Courier Fraud"
    },
    {
        "question": "You start getting bills for a phone contract and credit cards you never applied for. After checking, you find out someone used your name and details.",
        "answer": "Identity Fraud"
    },
    {
        "question": "You’re offered a remote job but are told you must pay £50 upfront for training and equipment. Once you pay, the company disappears.",
        "answer": "Recruitment Fraud"
    },
    {
        "question": "You see an advert online for a brand-new smartphone at a great price. The seller asks for a direct bank transfer. After payment, you never receive the phone.",
        "answer": "Online Shopping and Auction Site Fraud"
    },
    {
        "question": "A person approaches you claiming you qualify for a government grant. But to receive it, you must first pay a processing fee. After you pay, they disappear.",
        "answer": "Advance Fee Fraud"
    },
    {
        "question": "You get an email appearing to be from HMRC, saying you're owed a tax refund. It asks you to input your bank details. Later, money is withdrawn from your account.",
        "answer": "Authorised Push Payment (APP) Fraud"
    },
    {
        "question": "Your internet stops working. You get a call from someone claiming to be from your provider, who asks you to install a program so they can fix the issue. Afterwards, you’re charged and your files are missing.",
        "answer": "Computer Software Service Fraud"
    },
    {
        "question": "A friend recommends a business offering huge returns on cryptocurrency investments. You invest £3,000, then the company stops responding.",
        "answer": "Investment Fraud"
    },
    {
        "question": "You pay for two airline tickets through a third-party website. When you arrive at the airport, the airline has no record of your booking.",
        "answer": "Ticketing Fraud"
    }
]

# List of all scam types to use as multiple-choice options
all_scam_types = list(set(item["answer"] for item in quiz_data))

score = 0

for idx, item in enumerate(quiz_data, 1):
    print(f"\nQuestion {idx}:")
    print(item["question"])
    
    # Get 3 incorrect answers
    wrong_answers = random.sample([scam for scam in all_scam_types if scam != item["answer"]], 3)
    options = wrong_answers + [item["answer"]]
    random.shuffle(options)
    
    # Print choices
    option_map = {}
    for i, opt in enumerate(options):
        letter = chr(65 + i)  # A, B, C, D
        option_map[letter] = opt
        print(f"  {letter}. {opt}")
    
    # Get user input
    user_answer = input("Your answer (A, B, C, D): ").strip().upper()
    
    if user_answer in option_map and option_map[user_answer] == item["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer was: {item['answer']}")

# Final score
print(f"\nYour final score: {score} out of {len(quiz_data)}")
