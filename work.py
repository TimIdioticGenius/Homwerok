class WordsFinder:
    def __init__(self,*files):
        self.file_names=list(files)
        self.words_dict={}
    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name,'r') as file:
                words=file.read().split()
                self.words_dict[file_name]=words
        return self.words_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова