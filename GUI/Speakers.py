#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gtts import gTTS


# # Direct download from AO3

# In[2]:


import AO3


# In[ ]:


work_id = 17122361


# In[3]:


work = AO3.Work(work_id)
work.load_chapters()

print(work.title)
print('Number of chapters:', work.chapters)

for i in range(work.chapters):
    i += 1
    text = work.get_chapter_text(i)
    
    tts = gTTS(text)
    tts.save(work.title + 'CH' + str(i) + '.mp3')
    
    print('Chapter %i is saved' % i)
    
print('Work Saved!')


# # From pdf

# In[2]:


import fitz
import numpy as np


# In[ ]:


pdf_document = "eighteen wheels on an.pdf"


# In[3]:


doc = fitz.open(pdf_document)  
#print ("number of pages: %i" % doc.pageCount)
  
book_marks = np.array(doc.getToC())[1:,2]
book_marks = np.append(book_marks, doc.pageCount)

for i in range(len(book_marks) - 1):
    chapter_text = str()
    
    for j in range(int(book_marks[i]), int(book_marks[i+1])):
        page = doc.loadPage(j - 1)  
        page_text = page.getText("text")  
        chapter_text += page_text 
    
    i += 1
    
    chapter_text = chapter_text.replace('\n', ' ')

    ts = gTTS(chapter_text)
    ts.save(pdf_document.split('.pdf')[0] + ' CH' + str(i) + '.mp3')
    
    print('Chapter %i is saved' % i)
    
print('Work Saved!')


# # Inbuilt Display 

# In[ ]:


from IPython.display import Audio


# In[3]:


Audio('')

