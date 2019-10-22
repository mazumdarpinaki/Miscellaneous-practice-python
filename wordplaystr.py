class wordplaystr(str):
    '''A string that can report whether it has interesting properties'''

    def same_start_and_end(self):
        '''(wordplaystr)-> bool
        Return whether first and last letters are same
        precondition: len(self) !=0
        >>>s=wordplaystr('abracadabra')
        >>>s.same_start_and_end('abracadabr')
        'True'
        >>>s=wordplaystr('abcdeon')
        >>>s.same_start_and_end('abcdeon')
        'True'
        '''
        return self[0]==self[-1]

    import doctest
    doctest.testmod()

    
