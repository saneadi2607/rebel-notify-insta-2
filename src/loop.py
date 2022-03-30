import random
from dhooks import Webhook
import dhooks

from src.config import Config
from src.instagram.post import Post
from src.instagram.scraper import Scraper
from src.instagram.user import User

COLORS = [0xFFFFFF]

class Loop:
    def __init__(self, config: Config, username):
        self.webhook = Webhook(config.webhook_url)
        self.username = username
        self.last_image = 0

    def run(self, cycle):
        print(f'    [USER MONITOR] Checking profile @{self.username} of Cycle #{cycle}.')
        scraper = Scraper(self.username)
        post = scraper.get_last_post()
        user = scraper.get_user()
        print(f'        [EVENT] KEYWORDS FOUND: Dunk [{"dunk" in post.caption.lower()}], Jordan [{"jordan" in post.caption.lower()}], Yeezy [{"yeezy" in post.caption.lower()}], YZY [{"yzy" in post.caption.lower()}]')
        print(f'        [LOG] LAST KEYWORD MATCH IMAGE ID: {self.last_image}')
        if post.id != self.last_image :     
                embed = self.__create_embed(post, user)
                print(f'        [LAST LOAD EVENT] New post found\n{user.name} : {post.id}')
                if cycle == 0:
                    print('         [INITIAL TRIGGER] Profile Loaded')
                else:
                    print(f'        [TRIGGER EVENT] NEW POST DETECTED {post.id} - WEBHOOK SENT!')
                    self.webhook.send(embed=embed)
        
        self.last_image = post.id
        return

    @staticmethod
    def __create_embed(post: Post, user: User) -> dhooks.Embed:
        embed = dhooks.Embed(description=f"**CAPTION:** \n {post.caption}")
        embed.color = random.choice(COLORS)
        embed.add_field(name='POST:',value=f"[**[LINK TO INSTRAGRAM POST](https://www.instagram.com/p/{post.post_link})**]")
        embed.set_image(post.image_url)
        embed.set_timestamp(time=post.timestamp)
        embed.set_footer(text="Rebel Notify", icon_url="https://i.imgur.com/x9Vsn7m.jpg")
        embed.set_author(name=user.name, icon_url=user.icon_url, url=user.link)

        return embed
