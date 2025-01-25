import streamlit as st

# Define the questions and options
questions = [
    "What is your coaching business name?",
    "What type of coaching do you specialize in?",
    "Who is your target audience?",
    "What is your unique coaching approach?",
    "What are your main coaching programs or services?",
    "What is your pricing model?",
    "What is your marketing strategy?",
    "Who are your main competitors?",
    "What are your financial projections for the next year?",
    "What are your long-term goals as a coach?"
]

options = {
    "What type of coaching do you specialize in?": ["Life Coaching", "Career Coaching", "Executive Coaching", "Health and Wellness Coaching", "Other"],
    "Who is your target audience?": ["Individuals", "Professionals", "Entrepreneurs", "Students", "Other"],
    "What is your unique coaching approach?": ["Holistic Approach", "Goal-Oriented", "Mindfulness-Based", "Strengths-Based", "Other"],
    "What are your main coaching programs or services?": ["One-on-One Coaching", "Group Coaching", "Online Courses", "Workshops", "Other"],
    "What is your pricing model?": ["Hourly Rate", "Package Deals", "Subscription Model", "Pay-What-You-Can", "Other"],
    "What is your marketing strategy?": ["Social Media", "Email Marketing", "Networking Events", "Referrals", "Other"],
    "Who are your main competitors?": ["Local Coaches", "Online Coaching Platforms", "Wellness Centers", "Other"],
    "What are your financial projections for the next year?": ["< $50,000", "$50,000 - $100,000", "$100,000 - $200,000", "> $200,000"],
    "What are your long-term goals as a coach?": ["Expand Client Base", "Publish a Book", "Launch an Online Platform", "Mentor New Coaches", "Other"]
}

# Pre-written paragraphs for each option
paragraphs = {
    "What type of coaching do you specialize in?": {
        "Life Coaching": "As a life coach, I specialize in helping individuals achieve personal growth and fulfillment. My focus is on empowering clients to overcome challenges and live their best lives.",
        "Career Coaching": "As a career coach, I assist professionals in navigating their career paths, making strategic decisions, and achieving their professional goals.",
        "Executive Coaching": "As an executive coach, I work with leaders to enhance their leadership skills, improve team performance, and drive organizational success.",
        "Health and Wellness Coaching": "As a health and wellness coach, I support clients in achieving their physical and mental well-being through personalized coaching and actionable strategies.",
        "Other": "My coaching specialization is unique and tailored to meet the specific needs of my clients. I am committed to delivering impactful results."
    },
    "Who is your target audience?": {
        "Individuals": "My target audience is individuals seeking personal growth and transformation. I provide personalized coaching to help them achieve their goals.",
        "Professionals": "My target audience is professionals looking to advance their careers and improve their work-life balance. I offer tailored coaching programs to meet their needs.",
        "Entrepreneurs": "My target audience is entrepreneurs who want to grow their businesses and overcome challenges. I provide strategic coaching to help them succeed.",
        "Students": "My target audience is students who need guidance in achieving their academic and personal goals. I offer coaching to help them thrive.",
        "Other": "My target audience is unique and requires a customized approach. I am dedicated to understanding their needs and delivering value."
    },
    "What is your unique coaching approach?": {
        "Holistic Approach": "My coaching approach is holistic, addressing all aspects of a client's life to ensure balanced and sustainable growth.",
        "Goal-Oriented": "My coaching approach is goal-oriented, helping clients set and achieve clear, actionable objectives.",
        "Mindfulness-Based": "My coaching approach is mindfulness-based, focusing on self-awareness and present-moment focus to drive positive change.",
        "Strengths-Based": "My coaching approach is strengths-based, helping clients leverage their unique strengths to achieve success.",
        "Other": "My coaching approach is tailored to the individual needs of my clients, ensuring personalized and effective results."
    },
    "What are your main coaching programs or services?": {
        "One-on-One Coaching": "My main service is one-on-one coaching, where I provide personalized support to help clients achieve their goals.",
        "Group Coaching": "My main service is group coaching, offering a collaborative environment for clients to learn and grow together.",
        "Online Courses": "My main service is online courses, providing flexible and accessible learning opportunities for clients.",
        "Workshops": "My main service is workshops, delivering intensive and interactive coaching experiences.",
        "Other": "My coaching programs and services are customized to meet the unique needs of my clients."
    },
    "What is your pricing model?": {
        "Hourly Rate": "My pricing model is based on an hourly rate, providing flexibility for clients to book sessions as needed.",
        "Package Deals": "My pricing model includes package deals, offering clients discounted rates for multiple sessions.",
        "Subscription Model": "My pricing model is a subscription-based approach, providing ongoing coaching support for a fixed monthly fee.",
        "Pay-What-You-Can": "My pricing model is pay-what-you-can, ensuring accessibility for clients with varying budgets.",
        "Other": "My pricing model is tailored to meet the needs of my clients and align with my business goals."
    },
    "What is your marketing strategy?": {
        "Social Media": "My marketing strategy focuses on social media, where I engage with my audience and share valuable content to attract clients.",
        "Email Marketing": "My marketing strategy includes email marketing, where I communicate directly with potential clients and share updates.",
        "Networking Events": "My marketing strategy involves attending networking events to build relationships and grow my client base.",
        "Referrals": "My marketing strategy relies on referrals, leveraging satisfied clients to recommend my services to others.",
        "Other": "My marketing strategy is customized to reach my target audience effectively and grow my coaching business."
    },
    "Who are your main competitors?": {
        "Local Coaches": "My main competitors are local coaches who offer similar services. I differentiate myself through my unique approach and personalized coaching.",
        "Online Coaching Platforms": "My main competitors are online coaching platforms that provide scalable solutions. I stand out by offering a more personalized experience.",
        "Wellness Centers": "My main competitors are wellness centers that offer holistic services. I focus on delivering specialized coaching to meet my clients' needs.",
        "Other": "My main competitors are unique to my niche. I continuously adapt my strategies to stay competitive."
    },
    "What are your financial projections for the next year?": {
        "< $50,000": "My financial projections for the next year are modest, with revenues expected to be under $50,000. I am focused on building a strong foundation for future growth.",
        "$50,000 - $100,000": "My financial projections for the next year are promising, with revenues expected to be between $50,000 and $100,000. I am optimistic about my growth potential.",
        "$100,000 - $200,000": "My financial projections for the next year are strong, with revenues expected to be between $100,000 and $200,000. I am well-positioned for significant growth.",
        "> $200,000": "My financial projections for the next year are exceptional, with revenues expected to exceed $200,000. I am on track to achieve remarkable success."
    },
    "What are your long-term goals as a coach?": {
        "Expand Client Base": "My long-term goal is to expand my client base, reaching more individuals who can benefit from my coaching services.",
        "Publish a Book": "My long-term goal is to publish a book, sharing my expertise and insights with a wider audience.",
        "Launch an Online Platform": "My long-term goal is to launch an online platform, offering scalable coaching solutions to clients worldwide.",
        "Mentor New Coaches": "My long-term goal is to mentor new coaches, helping them develop their skills and grow their own coaching businesses.",
        "Other": "My long-term goals are tailored to my unique vision and mission as a coach."
    }
}

# Initialize session state to store answers
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Function to generate the business plan with specific paragraphs
def generate_business_plan(answers):
    business_plan = f"""
    # Coaching Business Plan for {answers[questions[0]]}

    ## Coaching Specialization
    {paragraphs[questions[1]][answers[questions[1]]]}

    ## Target Audience
    {paragraphs[questions[2]][answers[questions[2]]]}

    ## Unique Coaching Approach
    {paragraphs[questions[3]][answers[questions[3]]]}

    ## Coaching Programs and Services
    {paragraphs[questions[4]][answers[questions[4]]]}

    ## Pricing Model
    {paragraphs[questions[5]][answers[questions[5]]]}

    ## Marketing Strategy
    {paragraphs[questions[6]][answers[questions[6]]]}

    ## Competitors
    {paragraphs[questions[7]][answers[questions[7]]]}

    ## Financial Projections
    {paragraphs[questions[8]][answers[questions[8]]]}

    ## Long-Term Goals
    {paragraphs[questions[9]][answers[questions[9]]]}

    ## Conclusion
    This business plan outlines the strategic direction of {answers[questions[0]]}. I am confident in my ability to achieve my goals and make a positive impact through my coaching.
    """
    return business_plan

# Streamlit app
st.title("Coaching Business Plan Generator")

# Ask the questions
for i, question in enumerate(questions):
    if question in options:
        st.session_state.answers[question] = st.selectbox(question, options[question], key=f"q{i}")
    else:
        st.session_state.answers[question] = st.text_input(question, key=f"q{i}")

# Submit button
if st.button("Submit"):
    if all(st.session_state.answers.values()):
        business_plan = generate_business_plan(st.session_state.answers)
        st.subheader("Your Coaching Business Plan")
        st.markdown(business_plan)
    else:
        st.error("Please answer all the questions before submitting.")