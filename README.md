# UBCStudyAssist

UBCStudyAssist is an AI-powered web application designed to empower students at the University of British Columbia (UBC) and beyond by providing personalized study strategies tailored to their individual needs and academic goals. The app leverages the latest advancements in Large Language Models (LLMs) to create an intelligent chatbot that helps students develop effective and customized study plans.

## How It Works:
UBCStudyAssist begins by asking students a series of targeted questions about their study habits, preferred learning methods, and the courses they are currently enrolled in. By analyzing this input with LLM technology, the chatbot identifies the most effective study habits, techniques, and schedules that align with the student’s unique preferences and goals.

The app is particularly adept at understanding the nuances of different types of courses and subjects. Whether it's a content-heavy humanities course, a problem-solving-oriented math class, or a fast-paced computer science program, UBCStudyAssist provides tailored recommendations to suit the specific demands of each discipline.

### Key Features:
- **Personalized Study Technique Recommendations**: Get tailored study techniques based on your learning style, the subject you are studying, and how much time you have.
- **Course-specific Recommendations**: Receive study tips and strategies that are specifically designed to help you succeed in a particular course or subject.
- **. Guidance on Proven Study Habits**: Discover proven study habits that can help you stay focused and productive in your studies.
- **AI-powered Chatbot**: An intelligent assistant that guides you through selecting the best study method for any situation.
- **Location-based Study Spot Finder**: Use the OpenRoute PHI 4 API to discover quiet study spots across UBC and get directions to them.
- **Dynamic and Responsive Interface**: Built with Streamlit, offering an intuitive user experience with real-time chatbot responses.

This project aims to enhance the student experience by integrating AI with real-world campus navigation, helping students stay organized, productive, and on top of their studies.

## Why UBCStudyAssist Stands Out:
Studying at a university like UBC can be challenging, with students facing rigorous coursework and a wide range of disciplines. UBCStudyAssist simplifies this complexity by combining state-of-the-art AI with practical advice to help students thrive.

The app serves as more than just a study tool—it’s like having a personal academic coach available 24/7. By catering to a broad audience and offering scalable, customizable solutions, UBCStudyAssist is a transformative resource for any student looking to unlock their full potential.

Whether you’re new to university or looking to optimize your current study methods, UBCStudyAssist is the ultimate companion for achieving academic success.


## Getting Started

### Prerequisites
- Python 3.8+
- pip or poetry

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/UBCStudyBot.git
cd UBCStudyBot
```

### 2. Create OpenRouter API Key
1. Visit [OpenRouter.ai](https://openrouter.ai/)
2. Sign up for an account
3. Navigate to API Keys section
4. Generate a new API key

### 3. Environment Setup

#### Using Poetry (Recommended)
```bash
poetry install
poetry shell
```

#### Using pip
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Configure API Key
Create a `.env` file in the project root with your OpenRouter API key:
```
OPEN_ROUTER_KEY=your_openrouter_api_key_here
```

### 5. Run the Application
```bash
streamlit run app.py
```

## Important Notes
- The application uses the Gemini Flash model from OpenRouter by default
- Ensure you have a stable internet connection
- API usage is subject to OpenRouter's pricing and terms

## Troubleshooting
- If you encounter API key issues, double-check your `.env` file
- Verify that all dependencies are correctly installed
- Check your internet connection

## Resources and Learning Materials

### Study Techniques and Academic Success
- [UC Berkeley Study Skills](https://study.berkeley.edu/tips-and-tools/study-skills) - Comprehensive guide to effective studying
- [MIT OpenCourseWare Learning Resources](https://ocw.mit.edu/courses/learning-resources/) - Free learning materials and study strategies
- [Coursera Learning How to Learn](https://www.coursera.org/learn/learning-how-to-learn) - Popular course on effective learning techniques

### AI and Educational Technology
- [OpenRouter AI Documentation](https://openrouter.ai/docs) - API documentation for the AI service used
- [Streamlit Documentation](https://docs.streamlit.io/) - Learn more about the web app framework

### Related Projects and Inspirations
- [OpenRouterChatApp](https://github.com/mshojaei77/OpenRouterChatApp) - For Chatbot functionality


## Disclaimer
UBCStudyAssist is an experimental project and should be used as a supplementary tool alongside professional academic advice. Always consult with academic advisors, professors, and university resources for personalized guidance.

## Contributing / Get in Touch
Contributions are welcome! Please feel free to submit a Pull Request or contact me at owenhochwald@gmail.com.

## License
Apache License
