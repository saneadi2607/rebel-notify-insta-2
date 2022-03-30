from datetime import datetime


class Post:
    def __init__(self, json):
        self.json = json

    @property
    def caption(self) -> str:
        try:
            post_caption = self.json['edge_media_to_caption']['edges'][0]['node']['text']
        except:
            post_caption = "No caption found!"
        return post_caption

    @property
    def image_url(self):
        return self.json['display_url']

    @property
    def timestamp(self) -> datetime:
        timestamp = self.json['taken_at_timestamp']
        return datetime.utcfromtimestamp(timestamp)

    @property
    def comments(self) -> int:
        return self.json['edge_media_to_comment']['count']

    @property
    def likes(self) -> int:
        return self.json['edge_liked_by']['count']

    @property
    def id(self) -> int:
        try:
            post_id = self.json['id']
        except:
            post_id = 0
        return post_id

    @property
    def username(self) -> str:
        return self.json['username']

    @property
    def pfp_url(self) -> str:
        return self.json['profile_pic_url']
   
    @property
    def post_link(self) -> str:
        return self.json['shortcode']
