# docx-translator
**Inspiration**:
My sister would translate my father's sermons from Korean to English. She would occasionally ask me if I could just copy and paste from Google Translate to help her out. Then, she could just fix the grammar. Thus, I decided to try and automate this task because I'd rather watch a show than spend half an hour wearing out my keys.

**How to Use**:
1. Go to the directory the project is in. For example, mine is "C:\Users\peter\PycharmProjects\docx-translator>"
2. activate venv
  a. for Windows: `venv\Scripts\activate`  
4. run main.py with `python main.py`

there are 4 optional arguments.
1. -i - the path the program should import from (ie. the document that should be translated)
2. -o - the path the program should export to (ie. the document that should be made after translating)
3. -src - the source language (ie. the language to translate from)
4. -dest - the target language (ie. the language to translate to)

- if -i is not given, then a QFileDialog will pop up.
- if -o is not given, then the default path "project-directory/new/translated.docx" will be used
- if -src is not given, then the source language is assumed to be korean
- if -dest is not given, then the target language is assumed to be english

ex:
1. `cd PycharmProjects\docx-translator`
2. `venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `python main.py -i C:\Users\peter\PycharmProjects\docx-translator\test.docx -o C:\Users\peter\PycharmProjects\docx-translator\new\translated.docx -src ko -dest fr`
5. `deactivate`


TODO:
1. use official GoogleTrans API.
2. translate only words in src_lang to target_lang.
3. make a way for the user to not have to write the cwd in the paths.
4. change the name of the styles...
