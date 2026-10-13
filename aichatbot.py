import streamlit as st

st.set_page_config(page_title="AI & Course Chatbot", page_icon="🤖", layout="wide")
st.title("AI & Course Chatbot")
st.write("Welcome to the AI & Course Chatbot! Ask me anything about Python, AI, ML, courses, internships, or projects.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_bot_response(question):
    question = question.lower()
    words = question.split()

    # Greeting
    if "hello" in words or "hi" in words:
        return "Hello! How can I assist you today?"

    # Course
    elif "course" in question:
        if "available" in question:
            return "We offer courses in Python, Java, Web Development, and AI/ML."
        elif "join" in question or "enroll" in question or "register" in question:
            return "You can register for the course through the student portal."
        elif "long" in question or "duration" in question:
            return "The course duration depends on the selected course."
        elif "certificate" in question:
            return "Yes, you can receive a certificate after successfully completing the course requirements."
        elif "more" in question:
            return "Yes, you can learn multiple courses if they are available to you."
        elif "skill" in question or "skills" in question:
            return "You can learn programming, problem-solving, practical technical skills, and other skills related to the selected course."
        elif "criteria" in question or "eligibility" in question:
            return "Eligibility criteria may vary based on the course. Please check the official website for details."

    # Internship
    elif "internship" in question or "internships" in question:
        if "apply" in question:
            return "Apply through the official website or internship portal."
        elif "type" in question or "types" in question:
            return "Python, Java, Web Development, AI/ML, Data Science."
        elif "paid" in question or "free" in question:
            return "Both paid and unpaid internships may be available."
        elif "long" in question or "duration" in question:
            return "The internship duration depends on the selected internship program."
        elif "criteria" in question or "eligibility" in question:
            return "Eligibility criteria may vary based on the internship program. Please check the official website for details."
        elif "benefits" in question or "advantages" in question or "benefit" in question:
            return "An internship helps you gain practical experience, improve your skills, build confidence, and strengthen your resume."
        elif "certificate" in question:
            return "Yes, you can receive a certificate after successfully completing the internship requirements."
        elif "skills" in question or "skill" in question:
            return "You can improve programming, problem-solving, communication, teamwork, and practical technical skills during the internship."

    # Deadline / Submission
    elif "deadline" in question or "submission" in question:
        return "The project should be submitted before the deadline mentioned by the organization."

    # Certificate
    elif "certificate" in question:
        if "download" in question or ("get" in question and "where" in question):
            return "You can download your certificate from the internship portal after it is issued."
        elif "when" in question:
            return "You will receive your certificate after successfully completing the internship requirements."
        elif "hard copy" in question:
            return "The certificate format depends on the organization. It may provide a soft copy or a hard copy."
        elif "useful" in question:
            return "Yes. An internship certificate can help show your internship experience on your resume."

    # Project
    elif "project" in question:
        if "submit" in question or "submission" in question:
            return "You can submit your project through the internship portal before the deadline."
        elif "review" in question or "feedback" in question:
            return "The project review and feedback will be provided by the organization after submission."
        elif "format" in question or "guidelines" in question:
            return "Please follow the project guidelines provided by the organization for submission."
        elif "help" in question or "assistance" in question:
            return "If you need help with your project, you can reach out to your mentor or the support team."
        else:
            return "The project is designed to provide practical experience by applying programming concepts to a real-world problem."

    # Python
    elif (
        "python" in question
        or "numpy" in question
        or "pandas" in question
        or "matplotlib" in question
        or "tensorflow" in question
    ):
        if "libraries" in question or "library" in question:
            return "Some popular Python libraries include NumPy, Pandas, Matplotlib, and TensorFlow."
        elif "numpy" in question:
            return "NumPy is a library in Python used for numerical computing and working with arrays."
        elif "pandas" in question:
            return "Pandas is a library in Python used for data manipulation and analysis, providing data structures like DataFrames."
        elif "matplotlib" in question:
            return "Matplotlib is a library in Python used for creating static, animated, and interactive visualizations."
        elif "tensorflow" in question:
            return "TensorFlow is an open-source library in Python used for machine learning and deep learning applications."
        elif "variable" in question:
            return "A variable is used to store data in Python."
        elif "list" in question:
            return "A list is a collection in Python that is ordered, changeable, and allows duplicate values."
        elif "tuple" in question:
            return "A tuple is an ordered and unchangeable collection in Python."
        elif "dictionary" in question:
            return "A dictionary stores data in key-value pairs."
        elif "function" in question:
            return "A function is a reusable block of code that performs a specific task."
        elif "if statement" in question:
            return "An if statement is used to execute code when a condition is true."
        elif "for loop" in question:
            return "A for loop is used to repeat code for each item in a sequence."
        elif "while loop" in question:
            return "A while loop repeats code as long as a condition is true."
        elif "data type" in question or "data types" in question:
            return "Common Python data types include int, float, str, bool, list, tuple, set, and dictionary."
        elif "integer" in question:
            return "An integer is a whole number, such as 10, 25, or -5."
        elif "string" in question:
            return "A string is a sequence of characters written inside quotes."
        elif "boolean" in question:
            return "A Boolean represents one of two values: True or False."
        elif "operators" in question:
            return "Python operators are used to perform operations on values and variables."
        elif "arithmetic operator" in question:
            return "Arithmetic operators perform mathematical operations such as +, -, *, /, and %."
        elif "comparison operator" in question:
            return "Comparison operators compare values using operators like ==, !=, >, <, >=, and <=."
        elif "logical operator" in question:
            return "Logical operators combine conditions using and, or, and not."
        elif "exception handling" in question:
            return "Exception handling is used to handle errors in a Python program without stopping the program."
        elif "try except" in question:
            return "try and except are used to handle errors that may occur while running a Python program."
        elif "error" in question:
            return "An error is a problem in a program that can prevent it from running correctly."
        elif "oops" in question or "oop" in question or "object oriented programming" in question:
            return "OOP is a programming approach based on objects and classes."
        elif "class" in question:
            return "A class is a blueprint for creating objects in Python."
        elif "object" in question:
            return "An object is an instance of a class."
        elif "django" in question:
            return "Django is a Python web framework used to build web applications."
        elif "flask" in question:
            return "Flask is a lightweight Python web framework used to build web applications and APIs."
        elif "web development" in question:
            return "Python can be used for web development using frameworks like Django and Flask."
        elif "why" in question and "learn" in question:
            return "Python is useful to learn because it is easy to understand, widely used, and helpful in web development, data science, AI, automation, and more."
        elif "benefits" in question and "learn" in question:
            return "Learning Python can help you build programming skills, solve problems, create projects, and explore areas like AI, data science, web development, and automation."
        elif "advantages" in question:
            return "Python is known for its simplicity, readability, versatility, and large community support."
        elif "job" in question or "career" in question:
            return "Learning Python can run lead to job opportunities in web development, data science, AI, automation, and more."
        elif "easy" in question or "simple" in question:
            return "Yes, Python is considered one of the easiest programming languages to learn due to its simple syntax and readability."
        elif "learn" in question:
            return "You can learn Python by practicing basics, solving coding problems, building small projects, and practicing regularly."
        elif "practice" in question or "practicing" in question:
            return "You can practice Python by solving coding problems, building small projects, and using online platforms like LeetCode, HackerRank, or Codewars."
        elif "real-world" in question or "applications" in question:
            return "Python is used in web development, data analysis, artificial intelligence, machine learning, automation, and more."
        elif "used" in question or "use" in question:
            return "Python can be used for web development, data analysis, artificial intelligence, automation, and more."
        else:
            return "Python is a versatile programming language used for web development, data analysis, artificial intelligence, and more."

    # Artificial Intelligence
    elif "artificial intelligence" in question or " ai " in question:
        return "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence."

    # Machine Learning
    elif "machine learning" in question or " ml " in question:
        return "Machine Learning is a part of AI that allows computers to learn from data and make predictions."

    # Deep Learning
    elif "deep learning" in question:
        return "Deep Learning is a type of machine learning that uses neural networks with multiple layers."

    # Thank you
    elif "thank" in question or "thanks" in question:
        return "You're welcome! If you have any more questions, feel free to ask."

    # Exit keywords
    elif question in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day!"

    # Unknown question
    else:
        return "I'm still learning. Please ask me about Python, AI, ML, courses, internships, or projects."

# Accept user input via Streamlit chat input widget
if prompt := st.chat_input("Ask your question:"):
    # Append user message to state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot response
    response = get_bot_response(prompt)
    
    # Append assistant response to state and display it
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)