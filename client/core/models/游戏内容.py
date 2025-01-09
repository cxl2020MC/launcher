from pydantic import BaseModel


class Image(BaseModel):
    url: str
    link: str
    login_state_in_link: bool


class Banner(BaseModel):
    id: str
    image: Image
    i18n_identifier: None | str = None


class Post(BaseModel):
    id: str
    type: str
    title: str
    link: str
    date: str
    login_state_in_link: bool
    i18n_identifier: None | str = None


class SocialMediaLink(BaseModel):
    title: str
    link: str
    login_state_in_link: bool


class SocialMedialist(BaseModel):
    id: str
    icon: Image
    qr_image: Image
    qr_desc: str
    links: list[SocialMediaLink]
    enable_red_dot: bool
    red_dot_content: None | str = None


class Game(BaseModel):
    id: str
    biz: str


class Content(BaseModel):
    game: Game
    language: str
    banners: list[Banner]
    posts: list[Post]
    social_media_list: list[SocialMedialist]


class 游戏内容(BaseModel):
    retcode: int
    message: str
    data: Content
