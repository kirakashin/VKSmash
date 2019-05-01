import pylast


class LastFM:
    def __init__(self):
        """
        Initialization of LastFM
        """
        self.API_KEY = "870c624f4f8f237ad4b2832540c71242"
        self.API_SECRET = "8a9b3e3799110d93db1fa3bd241cac5c"
        self.network = pylast.LastFMNetwork(api_key=self.API_KEY, api_secret=self.API_SECRET)
        self.state = 'state: home'
        self.artist = ''
        self.album = ''
        self.track = ''
        self.num = 0

    def artist_albums(self, artist, num):
        """
        Returning list of top albums
        :param artist:
        :param num:
        :return:
        """
        return self.network.get_artist(artist).get_top_albums(limit=num)

    def artist_tracks(self, artist, num):
        """
        Returning list of top tracks
        :param artist:
        :param num:
        :return:
        """
        return self.network.get_artist(artist).get_top_tracks(limit=num)

    def similar_track(self, artist, track, num):
        """
        Returning somilar tracks
        :param artist:
        :param track:
        :param num:
        :return:
        """
        return self.network.get_track(artist, track).get_similar(limit=num)
