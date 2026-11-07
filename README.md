\# College FAQ Chatbot using NLP



An interactive college FAQ chatbot built using Python and Natural Language Processing (NLP). It helps students find answers to common college-related questions through a Streamlit web interface.



\## Features



\- Answers college-related questions using a predefined FAQ dataset.

\- Text preprocessing using NLTK.

\- TF-IDF vectorization.

\- Cosine similarity for question matching.

\- Synonym expansion and stemming.

\- Similarity threshold for rejecting unrelated questions.

\- Interactive Streamlit chat interface.

\- Suggested questions and conversation clearing.

\- Evaluation script for testing chatbot performance.



\## Technologies Used



| Technology | Purpose |

|---|---|

| Python | Core programming language |

| NLTK | Text preprocessing and stemming |

| Scikit-learn | TF-IDF and cosine similarity |

| Streamlit | Web interface |

| JSON | FAQ dataset storage |



\## Project Structure



```text

FAQ-Chatbot-NLP/

├── data/

│   └── faqs.json

├── app.py

├── chatbot.py

├── preprocess.py

├── evaluate.py

├── requirements.txt

├── README.md

└── .gitignore

```



\## How It Works



1\. User enters a question.

2\. The chatbot preprocesses the text.

3\. Synonyms are expanded and words are stemmed.

4\. TF-IDF converts text into numerical vectors.

5\. Cosine similarity compares the question with stored FAQs.

6\. The closest matching FAQ is selected.

7\. A similarity threshold determines whether to answer or return a fallback response.



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



\### 2. Navigate to the project folder



```bash

cd FAQ-Chatbot-NLP

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the environment



Windows PowerShell:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### 5. Install dependencies



```bash

pip install -r requirements.txt

```



\### 6. Run the application



```bash

streamlit run app.py

```



Open the local URL displayed in the terminal, usually `http://localhost:8501`.



\## Evaluation



Run:



```bash

python evaluate.py

```



The evaluation script tests exact FAQ questions, paraphrased questions, and unrelated questions.



The current test suite contains 38 test cases. Its pass rate measures performance on this selected test set, not guaranteed real-world accuracy.



\## Limitations



\- Answers are limited to the predefined FAQ dataset.

\- TF-IDF relies primarily on lexical similarity.

\- Complex questions and unfamiliar wording may produce incorrect matches.

\- The evaluation dataset is relatively small.



\## Future Improvements



\- Expand the FAQ dataset.

\- Add spelling correction.

\- Improve semantic understanding using Sentence Transformers.

\- Improve intent recognition.

\- Deploy the application online.



\## Author



Developed as a Python and Natural Language Processing project.

