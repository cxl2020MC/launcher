interface Image {
    url: string;
    link: string;
    login_state_in_link: boolean;
}

interface Banner {
    id: string;
    image: Image;
    i18n_identifier: string;
}

interface Post {
    id: string;
    type: string;
    title: string;
    link: string;
    date: string;
    login_state_in_link: boolean;
    i18n_identifier: string;
}

interface SocialMediaLink {
    title: string;
    link: string;
    login_state_in_link: boolean;
}

interface SocialMediaIcon {
    url: string;
    hover_url: string;
    link: string;
    login_state_in_link: boolean;
    md5: string;
    size: number;
}

interface SocialMediaQRImage {
    url: string;
    link: string;
    login_state_in_link: boolean;
}

interface SocialMediaList {
    id: string;
    icon: SocialMediaIcon;
    qr_image: SocialMediaQRImage;
    qr_desc: string;
    links: SocialMediaLink[];
    enable_red_dot: boolean;
    red_dot_content: string;
}

interface Game {
    id: string;
    biz: string;
}

interface Content {
    game: Game;
    language: string;
    banners: Banner[];
    posts: Post[];
    social_media_list: SocialMediaList[];
}

export interface get_game_content {
    retcode: number;
    message: string;
    data: {
        content: Content;
    };
}
