import time

class Track:
    def __init__(self, title, duration, artist, text=None):
        self.title = title if type(title) is str else 'Без названия'
        self.__duration = Track.time_value(duration)
        if self.__duration:
            if len(duration) - len(duration.replace(':', '')) == 2:
                self.__hour, self.__min, self.__sec = map(int, duration.split(':'))
            else:
                self.__hour, self.__min, self.__sec = 0, *map(int, duration.split(':'))
        self.artist = artist if type(title) is str else None
        self.text = text
        self.current_time = 0
        self.__duration_in_sec = Track.time_to_sec(self.__duration)

    def __str__(self):
        s = str(self.title)
        if self.artist:
            s += ', ' + self.artist
        if self.__duration:
            s += ' - ' + self.__duration
        return s

    def __repr__(self):
        return self.__str__()

    def play(self, start='00:00', finish=None):
        if finish == None:
            finish = self.__duration
        Track.time_checking_exception(start)
        Track.time_checking_exception(finish)
        start = Track.time_to_sec(start)
        finish = Track.time_to_sec(finish)

        self.current_time = start
        print(self)
        step = 0
        rest = 0
        while self.current_time < finish:
            time.sleep(1)
            self.current_time += 1
            if self.current_time >= step * self.__duration_in_sec / 100:
                rest += 100 / self.__duration_in_sec - int(100 / self.__duration_in_sec) - int(rest)
                print('#' * (int(100 / self.__duration_in_sec) + int(rest)), end='')
                step += 1
        print()

    def show_text(self):
        print(self.text)

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        print('Access denied to ' + str(self) + '.duration')

    @duration.getter
    def duration(self):
        return self.__duration

    @staticmethod
    def time_value(time_str):
        Track.time_checking_exception(time_str)
        n = 0
        for x in time_str:
            if x == ':':
                n += 1

        if n == 2:
            h, m, s = map(int, time_str.split(':'))
            return '{h}:{m:0>2}:{s:0>2}'.format(h=h, m=m, s=s)
        elif n == 1:
            m, s = map(int, time_str.split(':'))
            return '{m}:{s:0>2}'.format(m=m, s=s)

    @staticmethod
    def time_to_sec(time_str):
        Track.time_checking_exception(time_str)
        n = 0
        for x in time_str:
            if x == ':':
                n += 1
        if n == 2:
            h, m, s = map(int, time_str.split(':'))
            return h * 60 * 60 + m * 60 + s
        elif n == 1:
            m, s = map(int, time_str.split(':'))
            return m * 60 + s

    @staticmethod
    def time_checking_exception(time_str):
        if type(time_str) is not str:
            raise ValueError('Time must have "hh:mm:ss" format.')
        if not time_str.replace(':', '').isdigit():
            raise ValueError('Time must have "hh:mm:ss" format.')
        n = 0
        for x in time_str:
            if x == ':':
                n += 1
        try:
            if n == 2:
                h, m, s = map(int, time_str.split(':'))
                if m > 59 or s > 59:
                    raise ValueError('Time must have "hh:mm:ss" format.')
            elif n == 1:
                m, s = map(int, time_str.split(':'))
                if m > 59 or s > 59:
                    raise ValueError('Time must have "hh:mm:ss" format.')
            else:
                raise ValueError('Time must have "hh:mm:ss" format.')
        except ValueError:
            raise ValueError('Time must have "hh:mm:ss" format.')


class Album:
    def __init__(self, title, year, *tracks):
        self.title = title if type(title) is str else None
        self.year = year if year.isdigit() and len(year) == 4 else None
        self.tracks = list(tracks)

    def __str__(self):
        s = 'Альбом ' + self.title + ', ' + self.year + ' г.\n'
        s += '------------------------------------------------\n'
        for i in range(len(self.tracks)):
            s += str(i + 1) + '. ' + str(self.tracks[i]) + '\n'
        return s

    def __repr__(self):
        return 'Альбом' + self.title + ', ' + self.year + ' год'

    def add_track(self, track):
        self.tracks.append(track)

    def play(self, start_track=0, finish_track=None):
        if finish_track == None:
            finish_track = len(self.tracks)
        for i in range(start_track, finish_track):
            self.tracks[i].play()
