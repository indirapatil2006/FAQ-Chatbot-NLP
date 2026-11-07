
from chatbot import FAQChatbot
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess_text

# Load chatbot
chatbot = FAQChatbot()

THRESHOLD = 0.25


def get_best_match(question):
    cleaned = preprocess_text(question)

    if not cleaned:
        return None, 0.0

    vector = chatbot.vectorizer.transform([cleaned])

    scores = cosine_similarity(
        vector, chatbot.question_vectors
    )

    index = scores.argmax()
    return index, float(scores[0][index])


# Exact FAQ tests
exact_tests = [
    faq["question"] for faq in chatbot.faqs
]

# Paraphrased questions with expected FAQ keywords
paraphrase_tests = [
    ("What time do classes begin?", "timing"),
    ("Where do I apply to join the college?", "admission"),
    ("Can students take books home?", "borrow"),
    ("Where can I see my attendance percentage?", "attendance"),
    ("Are there financial aid options?", "scholarship"),
    ("Does the college provide accommodation?", "hostel"),
    ("How can I get campus recruitment support?", "placement"),
    ("Where can I find internship opportunities?", "internship"),
]

# Unrelated questions
unrelated_tests = [
    "What is the capital of France?",
    "Who won the football World Cup?",
    "How do I make chocolate cake?",
    "What is the weather today?",
    "Tell me a joke.",
]


def find_expected_index(keyword):
    for i, faq in enumerate(chatbot.faqs):
        if keyword.lower() in faq["question"].lower():
            return i
    return None


print("\n" + "=" * 55)
print("       FAQ CHATBOT - EVALUATION REPORT")
print("=" * 55)

# 1. Exact tests
exact_passed = 0

print("\n1. EXACT FAQ TESTS\n")

for question in exact_tests:
    index, score = get_best_match(question)
    passed = index is not None and score >= THRESHOLD

    if passed:
        exact_passed += 1

    print(
        f"[{'PASS' if passed else 'FAIL'}] {question}"
        f" | Similarity: {score:.2f}"
    )

# 2. Paraphrase tests
paraphrase_passed = 0
paraphrase_total = 0

print("\n2. PARAPHRASED QUESTION TESTS\n")

for question, keyword in paraphrase_tests:
    expected = find_expected_index(keyword)
    predicted, score = get_best_match(question)

    if expected is None:
        print(f"[SKIP] No FAQ found for keyword: {keyword}")
        continue

    passed = predicted == expected and score >= THRESHOLD
    paraphrase_total += 1

    if passed:
        paraphrase_passed += 1

    matched = chatbot.faqs[predicted]["question"]

    print(f"[{'PASS' if passed else 'REVIEW'}] {question}")
    print(f"       Expected: {chatbot.faqs[expected]['question']}")
    print(f"       Matched:  {matched}")
    print(f"       Similarity: {score:.2f}\n")

# 3. Unrelated question tests
unrelated_passed = 0

print("\n3. UNRELATED QUESTION TESTS\n")

for question in unrelated_tests:
    index, score = get_best_match(question)
    passed = score < THRESHOLD

    if passed:
        unrelated_passed += 1

    print(
        f"[{'PASS' if passed else 'FAIL'}] {question}"
        f" | Similarity: {score:.2f}"
    )

# Final report
total_passed = (
    exact_passed + paraphrase_passed + unrelated_passed
)

total_tests = (
    len(exact_tests) + paraphrase_total + len(unrelated_tests)
)

pass_rate = (
    total_passed / total_tests * 100
    if total_tests else 0
)

print("\n" + "=" * 55)
print("                 FINAL SUMMARY")
print("=" * 55)

print(f"Exact FAQ tests:       {exact_passed}/{len(exact_tests)}")
print(f"Paraphrase tests:      {paraphrase_passed}/{paraphrase_total}")
print(f"Unrelated tests:       {unrelated_passed}/{len(unrelated_tests)}")
print("-" * 55)
print(f"Total passed:          {total_passed}/{total_tests}")
print(f"Test pass rate:        {pass_rate:.2f}%")
print("=" * 55)

print("\nNote: Test pass rate is not the same as real-world accuracy.")
