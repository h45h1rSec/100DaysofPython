# Build a program cablable of displaying questions to the user like KBC.
# Use list data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

Questions = [

    ["What does HTML stand for?", "Hyper Text Markup Language", "Highly Typed Modern Language", "Hyper Transfer Markup Language", "Home Tool Markup Language", 1],
    ["In programming, what is the process of finding errors and fixing them called?", "Debugging", "Compiling", "Testing", "Analyzing", 1],
    ["Which programming language is known for its readability and ease of learning?", "C++", "Java", "Python", "Ruby", 3],
    ["What is the purpose of a firewall in cybersecurity?", "To protect against viruses", "To prevent unauthorized access", "To encrypt data", "To monitor internet usage", 2],
    ["What is the term for a malicious software that disguises itself as something legitimate?", "Virus", "Worm", "Trojan Horse", "Spyware", 3],
    ["Which encryption algorithm is widely used for securing data transmitted over the internet?", "AES", "DES", "RSA", "MD5", 1],
    ["What does SQL stand for in the context of databases?", "Structured Query Language", "Simple Question Language", "Sequential Query Language", "Systematic Question Language", 1],
    ["What is the purpose of version control systems like Git?", "To track changes in code and collaborate on projects", "To compile code and generate executables", "To test software applications", "To manage database schemas", 1],
    ["Which programming language is commonly used for building dynamic web applications?", "Java", "C#", "JavaScript", "PHP", 3],
    ["What is the concept of 'phishing' in cybersecurity?", "A method of testing security vulnerabilities", "A technique for secure communication", "An attempt to trick individuals into revealing sensitive information", "A form of denial-of-service attack", 3],
    ["In object-oriented programming, what is encapsulation?", "A technique for organizing code into smaller units", "The process of converting code into machine language", "The bundling of data and methods that operate on the data", "A way to optimize code execution", 3],
    ["What is the purpose of an API (Application Programming Interface)?", "To create graphical user interfaces", "To enable communication between different software applications", "To store and retrieve data in a database", "To manage network security", 2],
    ["What is the difference between 'GET' and 'POST' in HTTP?", "GET is used for submitting form data, and POST is used for requesting data from a server", "GET is used for requesting data from a server, and POST is used for submitting form data", "There is no difference between GET and POST", "GET and POST are both used for secure encryption of data", 2],
    ["What is the primary function of an operating system?", "To run applications", "To manage hardware resources", "To design user interfaces", "To create backups of data", 2],
    ["What is the purpose of the 'if' statement in programming?", "To declare variables", "To loop through a collection", "To make decisions based on conditions", "To define functions", 3],
    ["What is a 'stack' in the context of data structures?", "A linear data structure that follows the Last In, First Out (LIFO) principle", "A hierarchical data structure", "An algorithm for sorting elements", "A way to represent relationships between entities", 1],
    ["What is the difference between 'compiler' and 'interpreter'?", "A compiler translates high-level code into machine code, while an interpreter executes code line by line", "A compiler interprets code line by line, while an interpreter translates high-level code into machine code", "There is no difference between a compiler and an interpreter", "A compiler and an interpreter perform the same functions", 1],
    ["What is 'Big O notation' used for in computer science?", "To represent the size of a data structure", "To measure the efficiency of algorithms in terms of time and space complexity", "To define the output of a program", "To indicate the order of execution of statements", 2],
    ["What is the concept of 'inheritance' in object-oriented programming?", "The ability of a class to inherit properties and behaviors from another class", "The process of creating an instance of a class", "The practice of sharing data between different classes", "The mechanism for defining variables in a class", 1],
    ["What is a 'Distributed Denial of Service (DDoS) attack'?", "An attack that aims to delete data from a server", "An attack that floods a system with traffic to make it unavailable", "An attack that steals sensitive information", "An attack that targets a specific individual's computer", 2],
    ["What is the purpose of the 'try', 'except', and 'finally' blocks in Python?", "To define variables", "To handle exceptions and errors", "To create loops", "To execute code repeatedly", 2],
    ["What is 'SQL injection' in the context of cybersecurity?", "A technique for injecting malware into a computer system", "A method of extracting information from a database", "A type of denial-of-service attack", "A method of exploiting vulnerabilities in SQL queries to gain unauthorized access", 4],
    ["What is the difference between 'symmetric' and 'asymmetric' encryption?", "Symmetric encryption uses the same key for both encryption and decryption, while asymmetric encryption uses different keys", "There is no difference between symmetric and asymmetric encryption", "Asymmetric encryption is used for securing communications, while symmetric encryption is used for file storage", "Symmetric encryption is more secure than asymmetric encryption", 1],
    ["What is 'cybersecurity hygiene'?", "Practices and measures to maintain good health in cyberspace", "A type of malware", "The use of virtual reality for cybersecurity", "The process of securing and protecting computer systems and networks", 4],
    ["What is 'agile methodology' in software development?", "A framework for managing hardware projects", "A method for rapidly developing and delivering software in small, incremental cycles", "A programming language", "A technique for debugging code", 2],
    ["What is the purpose of a 'keylogger' in cybersecurity?", "To track the physical location of a device", "To record keystrokes on a computer", "To generate cryptographic keys", "To block unauthorized access to a network", 2],
    ["What is the concept of 'cloud computing'?", "A type of programming language", "A method of storing data on physical servers", "A model for delivering computing services over the internet", "A technique for optimizing code execution", 3],
    ["What is 'two-factor authentication'?", "A method of encrypting data", "A technique for validating the identity of a user using two different methods", "A type of computer virus", "A way to improve internet speed", 2],
    ["What is the purpose of the 'grep' command in Unix/Linux?", "To display system information", "To search for a specific pattern in files", "To create a new file", "To delete files", 2]

]

Levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
Cash = 0

for Iterate in range(0, len(Questions)):

    CurrentQuestion = Questions[Iterate]
    print(f"\n\nYour Question for {Levels[Iterate]}$ Cash!")
    print(f"\n Question#{Questions.index(Questions[Iterate])+1} => {CurrentQuestion[0]}\n")
    print(f"1. {CurrentQuestion[1]}\t2. {CurrentQuestion[2]}\n3. {CurrentQuestion[3]}\t4. {CurrentQuestion[4]}")

    UserReply = int(input("\nEnter your answer (1, 2, 3, 4) or (Press 0 to quit): "))

    if UserReply == CurrentQuestion[-1]:
        print(f"Correct Answer! You have won {Levels[Iterate]}...")
        
        if(Iterate==4):
            Cash = 10000
        elif(Iterate==9):
            Cash = 320000
        elif(Iterate==14):
            Cash = 10000000

    elif UserReply == 0:
        print("OK, Exiting...")
        break

    else:
        print("\nIncorrect Answer!\nBetter luck next time!\nExiting...")
        break

print(f"You took {Cash} cash with you!")
