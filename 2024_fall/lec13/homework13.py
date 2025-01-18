import bs4

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    
    soup = bs4.BeautifulSoup(text, "html.parser")
    stories = []
    for item in soup.find_all('article'):
        title_tag = item.find('h3') 
        teaser_tag = item.find('p') 
      
        title = title_tag.text.strip() if title_tag else ''
        teaser = teaser_tag.text.strip() if teaser_tag else ''
        
        stories.append((title, teaser))
    
    return stories

import gtts

def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
   
    if n < 0 or n >= len(stories):
        raise ValueError(f"Invalid index {n}. Must be between 0 and {len(stories)-1}")
    
    title, teaser = stories[n]
    text = f"Title: {title}. Teaser: {teaser}" if teaser else f"Title: {title}."
    
    tts = gtts.gTTS(text=text, lang='en')
    tts.save(filename)
