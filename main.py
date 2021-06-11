from mrjob.job import MRJob
from mrjob.step import MRStep

Class txtBreakdown(MRJob):
    def setps(self):
        return  []
            MRStep(map= self.mapper,
                   reduce=self.reducer)

def mapper(self, _, line):
    word = line.split()
    yield word, 1


def reducer(self, key, values):
    yield key, sum(values)
    
if __name__== '__main__':
    txtBreakdown.run()