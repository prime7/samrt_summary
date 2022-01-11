import urllib.request
import bs4 as BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer


def get_contents(URL):
    fetched_data = urllib.request.urlopen(URL)
    article_read = fetched_data.read()
    article_parsed = BeautifulSoup.BeautifulSoup(article_read,'html.parser')
    paragraphs = article_parsed.find_all('p')
    
    content = ''
    for p in paragraphs:
        content += p.text
        
    content = re.sub(r'\[[0-9]*\]', ' ', content)
    content = re.sub(r'\s+', ' ', content) 
    content = re.sub(r'\([^)]*\)', '', content)
    
    return content

def parse_content(content):       
    content = re.sub(r'\[[0-9]*\]', ' ', content)
    content = re.sub(r'\s+', ' ', content) 
    content = re.sub(r'\([^)]*\)', '', content)
    
    return content


def _create_dictionary_table(text_string) -> dict:
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    stem = PorterStemmer()
    
    frequency_table = dict()
    for wd in words:
        wd = stem.stem(wd)
        if wd in stop_words:
            continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1

    return frequency_table


def _calculate_sentence_scores(sentences, frequency_table) -> dict:   
    sentence_weight = dict()
    for sentence in sentences:
        sentence_wordcount = (len(word_tokenize(sentence)))
        sentence_wordcount_without_stop_words = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                sentence_wordcount_without_stop_words += 1
                if sentence in sentence_weight:
                    sentence_weight[sentence] += frequency_table[word_weight]
                else:
                    sentence_weight[sentence] = frequency_table[word_weight]

        sentence_weight[sentence] = sentence_weight[sentence] / sentence_wordcount_without_stop_words

    return sentence_weight


def _calculate_average_score(sentence_weight) -> int:
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]

    average_score = (sum_values / len(sentence_weight))

    return average_score


def _get_article_summary(sentences, sentence_weight, threshold):
    sentence_counter = 0
    article_summary = ''

    for sentence in sentences:
        if sentence in sentence_weight and sentence_weight[sentence] >= (threshold):
            article_summary += " " + sentence
            sentence_counter += 1

    return article_summary


def _run_article_summary(article,MULTIPLIER):
    frequency_table = _create_dictionary_table(article)
    sentences = sent_tokenize(article)
    sentence_scores = _calculate_sentence_scores(sentences, frequency_table)
    threshold = _calculate_average_score(sentence_scores)
    article_summary = _get_article_summary(sentences, sentence_scores, MULTIPLIER * threshold)

    return article_summary


def run(URL,CONTENT):
    summary_results = ""
    if URL:
        summary_results = _run_article_summary(get_contents(URL),1.5)
    elif CONTENT:
        summary_results = _run_article_summary(parse_content(CONTENT),1.3)
    
    return summary_results