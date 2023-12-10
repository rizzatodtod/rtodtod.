from PIL import Image
import requests
import streamlit as st 


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- LOAD ASSETS ----

img_How_to_Overcome = Image.open("images/yt_How_to_Overcome.png")
img_Common_Problems = Image.open("images/yt_Common_Problems.png")


# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Rizza Mae A. Todtod :wave:")
    st.title("How To Overcome The Challenges In Computer Engineering")
    st.write("To overcome challenges in computer engineering, it is essential to continuously learn and stay updated with the latest technologies, develop strong fundamentals, approach problems with a systematic mindset, collaborate with others, gain hands-on experience, embrace failure as a learning opportunity, manage time effectively, and maintain persistence and motivation. By combining these strategies, one can navigate the complexities of computer engineering and successfully overcome challenges in the field.")
    st.write("[Learn More >](https://files.eric.ed.gov/fulltext/ED577147.pdf)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            How to Overcome the challenges of being a Computer Engineer:
            - CONTINOUOS LEARNING: To keep up with the newest technological advancements and trends, habitually read research papers, technical blogs, and articles.

            - PROBLE SOLVING SKILLS: To enhance problem-solving skills, seek advice from mentors and work alongside colleagues to gain fresh perspectives.

            - ADAPTABILITY: To take on new challenges, be willing to step out of your comfort zone and embrace changes.

            - COMMUNICATION SKILLS: In any engineering position, it is vital to have effective communication skills. Being able to express technical information in a concise and clear manner is necessary both orally and in writing.

            - TIME MANAGEMENT: Prioritizing tasks, managing time efficiently, and setting realistic deadlines are all crucial when dealing with the demanding workload of computer engineering. To prevent getting swamped, it's wise to break down massive assignments into more manageable segments and deal with them individually.

            - SOFT SKILL DEVELOPMENT: Engage in conversations, with your colleagues and mentors to receive feedback and pinpoint areas where you can enhance your skills. Take steps to actively develop and improve these skills.

            - WORK-LIFE BALANCE: Achieving long term success requires finding a balance, in life. It's important to avoid burnout by taking care of yourself both at work and, in your life. Make sure to take breaks prioritize self care and make time for your hobbies and things that bring you joy.
            """
    )
    st.write("[Learn More >](https://www.knowledgehut.com/blog/web-development/software-engineer-challenges)")
with right_column:
    st.empty()

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Overcome the Challenges in Computer Engineering")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_How_to_Overcome)
    with text_column:
        st.subheader("A Comprehensive Guide to Overcoming Challenges in Computer Engineering")
        st.write(
            """
            Learn how to overcome the challenges in Computer Engineer!
            Overcoming challenges in computer engineering requires a systematic approach that involves several key steps. Firstly, it is crucial to identify and understand the specific challenges you are facing. This could range from complex coding issues to hardware limitations. Once you have a clear understanding of the challenges, the next step is to research and gather relevant information. This could involve studying existing solutions, consulting experts, or exploring online resources.
            """
        )
        st.markdown("[Learn more ...>](https://spires.co/online-computer-science-tutors/undergraduate/overcoming-computer-science-challenges-common-problems-and-solutions)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Common_Problems)
    with text_column:
        st.subheader("A Practical Guide for Success")
        st.write(
            """
            Learn the effetive problem-solving in the realm of Computer Engineer!
            Effective problem-solving in the realm of computer engineering hones a mix of technical know-how, a proactive outlook, and adaptability. This manual highlights valuable techniques such as staying current with the latest advancements by staying educated continually, fostering teamwork as well as clear communication, and tackling complex issues systematically. These methods provide an edge in managing the ever-shifting tech landscape. Manage responsibilities and timing efficiently as well as maintain a healthy work-life equilibrium. To truly succeed in the ever-changing world of computer engineering, it's important to find guidance from experienced mentors as well as uphold a strong moral compass. In doing so, you'll develop the necessary tools to overcome obstacles and achieve personal development. Don't forget to embrace ethical responsibilities as you navigate this dynamic field.
            """
        )
        st.markdown("[Learn more...>](https://www.tatvasoft.com/outsourcing/2021/11/6-common-problems-in-the-software-development-process.html)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me !:")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Yourname" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="mmessage" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
