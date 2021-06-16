import time
import datetime
import threading
import decimal

class Tester:
    def __init__(self, paragraph):
        self.correctWords = []
        self.incorrectWords = {}
        self.typedWords = []
        self.totalWords = []
        self.input = None
        self.paragraph = paragraph
        self.accuracy = 0
        self.time = 0
        self.wordPerMin = 0
        self.run()

    def Clock(self):
        while len(self.typedWords) == 0:
            self.time += 1
            time.sleep(1)

    def run(self):
        threading.Thread(target=self.Clock).start()
        threading.Thread(target=self.TestSpeed).start()

    def TestSpeed(self):
        print('\n\n'+self.paragraph+'\n\n')
        self.input = str(input('\t\n'+'Start Typing..\n\n'))
        self.totalWords = self.paragraph.split(' ')
        self.typedWords = self.input.split(' ')

        try:
            for i in range(len(self.typedWords)):
                if(self.typedWords[i] == self.totalWords[i]):
                    self.correctWords.append(self.typedWords[i])
                else:
                    self.incorrectWords.update({self.totalWords[i] : self.typedWords[i]})

        except Exception as e:
            print(e)

        self.accuracy = round(len(self.correctWords)/len(self.typedWords) * 100, 2)
        self.wordPerMin = round(len(self.typedWords) / (self.time/60), 2)

        print('\n\nResults:--')
        print(f'Accuracy:-- {self.accuracy}')
        print(f'Word Per Minute:-- {self.wordPerMin}')
        print(f'Incorrect words:-- {self.incorrectWords}')


mytester = Tester('''A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea. A paragraph consists of one or more sentences. Though not required by the syntax of any language, paragraphs are usually an expected part of formal writing, used to organize longer prose.''')

