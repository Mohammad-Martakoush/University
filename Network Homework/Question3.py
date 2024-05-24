########################################
########## questions three #############

import json
import csv

def load_questions_from_json(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

def load_questions_from_csv(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append({"question": row["question"], "answer": row["answer"]})
    return questions

def ask_questions(questions):
    score = 0
    for i, q in enumerate(questions):
        user_answer = input(f"Q{i+1}: {q['question']} ")
        if user_answer.strip().lower() == q['answer'].strip().lower():
            score += 1
    return score

def save_result_to_json(file_path, user_name, score):
    result = {"user_name": user_name, "score": score}
    try:
        with open(file_path, 'r+') as file:
            data = json.load(file)
            data.append(result)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            json.dump([result], file, indent=4)

def save_result_to_csv(file_path, user_name, score):
    fieldnames = ['user_name', 'score']
    try:
        with open(file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"user_name": user_name, "score": score})
    except FileNotFoundError:
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"user_name": user_name, "score": score})

def main():
    file_path = input("Enter the path to the questions file (JSON or CSV): ")
    if file_path.endswith('.json'):
        questions = load_questions_from_json(file_path)
    elif file_path.endswith('.csv'):
        questions = load_questions_from_csv(file_path)
    else:
        print("Unsupported file format. Please use JSON or CSV.")
        return

    user_name = input("Enter your name: ")
    score = ask_questions(questions)
    print(f"{user_name}, your score is {score}/{len(questions)}")

    result_file_format = input("Enter the result file format to save (CSV or JSON): ")
    if result_file_format.lower() == 'json':
        save_result_to_json('results.json', user_name, score)
    elif result_file_format.lower() == 'csv':
        save_result_to_csv('results.csv', user_name, score)
    else:
        print("Unsupported result file format. Please use JSON or CSV.")

if __name__ == "__main__":
    main()

