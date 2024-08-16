from SimplerLLM.tools.serp import search_with_serpapi
import re
from typing import List

def search_chunk(chunk) -> List[str]:
    """
    Searches for a given chunk of text on the internet using SerperAPI which accesses Google's Engines.
    
    Parameters:
    - chunk: A string representing the text chunk to search for.
    
    Returns:
    - A boolean indicating whether the chunk was found online (True) or not (False).
    """
    list = []
    try:
        search_results = search_with_serpapi(f"\"{chunk}\"")
        found = len(search_results) > 0
        if (found):
            list.append(found)
            list.append(search_results[0].URL)
            return list
        else:
            list.append(found)
            list.append("None")
            return list
    except Exception as e:
        print(f"An error occurred: {e}")
        list.append(False)
        list.append("None")
        return list 

def chunk_text(text, chunk_by) -> List[str]:
    """
    Splits the input text into chunks based on the specified granularity (sentences or paragraphs).
    
    Parameters:
    - text: The input text to be chunked.
    - chunk_by: The granularity for chunking ('sentence' or 'paragraph').
    
    Returns:
    - A list of strings, where each string is a chunk of the original text.
    """
    if chunk_by == "sentence":
        sentences = re.split(r'(?<!\d)[.?!](?!\d)', text)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return sentences
    elif chunk_by == "paragraph":
        paragraphs = [paragraph.strip() for paragraph in text.split("\n") if paragraph.strip()]
        return paragraphs
    else:
        raise ValueError("Invalid chunk_by value. Choose 'sentence' or 'paragraph'.")

def calculate_plagiarism_score(text, chunk_by) -> float:
    """
    Calculates the plagiarism score of a given text by chunking it and checking each chunk for plagiarism.
    
    Parameters:
    - text: The input text to check for plagiarism.
    - chunk_by: The granularity for chunking the text ('sentence' or 'paragraph').
    
    Returns:
    - The plagiarism score as a float, representing the percentage of plagiarised content.
    """
    chunks = chunk_text(text, chunk_by)
    total_chunks = len(chunks)
    plagiarised_chunks = 0
    counter = 1
    for chunk in chunks:
        print(f"Chunk {counter} : {chunk} .... {search_chunk(chunk)[0]} .... {search_chunk(chunk)[1]}")
        counter += 1
        if search_chunk(chunk)[0]:
            plagiarised_chunks += 1

    
    plagiarism_score = (plagiarised_chunks / total_chunks) * 100 if total_chunks > 0 else 0
    return plagiarism_score


#MAIN SECTION
text = """ AI is changing digtal marketing and making it cooler than ever. yeah, it's not science fiction - it's 110 real.

In fact, AI is the secret sauce that's making brands sizzle like never before. Imagine AI as your creative buddy, helping with awesome copies, cool logos, and even sparking ideas. 

It's like having a an expert marketing friend with super powers. not kidding! In this post, I'll break down 11 awesome ways and examples on how to use AI in Marketing. 

sharing real practical use cases that helped me 10x my marketing results and save tons of hours! Many beginners miss out on email marketing, thinking it's not worth it.

However, it's proved that it has one of the highest ROIs with 44$ profit for every 1$ spent on it.

Email Marketing allows businesses to directly reach and engage their audience, fostering customer relationships and driving sales. 

It's a big part of my marketing strategy. """ # The Input Text
chunk_by = "sentence"  # "sentence" or "paragraph"
plagiarism_score = calculate_plagiarism_score(text, chunk_by)
print(f"Plagiarism Score: {plagiarism_score}%")