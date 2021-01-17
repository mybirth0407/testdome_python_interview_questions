class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        set_play = set()
        cursor = self
        while True:
            if cursor.next is None:
                return False
            if cursor.name in set_play:
                return True

            set_play.add(cursor.name)
            cursor = cursor.next

first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())