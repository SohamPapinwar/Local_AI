from text_extraction import extract_text_from_folder
from text_preprocessing import preprocess_text_from_dict
from question_answering import answer_question

def main(folder_path):
    # Extract text from folder
    extracted_text = extract_text_from_folder(folder_path)

    # Preprocess text
    preprocessed_text = preprocess_text_from_dict(extracted_text)

    # Answer questions based on preprocessed text
    for filename, text in preprocessed_text.items():
        question = input(f"Enter your question for file {filename}: ")
        answer = answer_question(question, text)
        print("Answer:", answer)

if __name__ == "__main__":
    folder_path = "folder_path"
    main(folder_path)
