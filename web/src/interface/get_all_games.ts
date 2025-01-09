interface Image {
    url: string;
    hover_url?: string;
    link: string;
    login_state_in_link: boolean;
    md5?: string;
    size?: number;
}

interface Display {
    language: string;
    name: string;
    icon: Image;
    title?: string;
    subtitle?: string;
    background: Image;
    logo: Image;
    thumbnail: Image;
    korea_rating?: any;
    shortcut?: Image;
}

interface Game {
    id: string;
    biz: string;
    display: Display;
    reservation?: any;
    display_status: string;
    game_server_configs: any[];
}

export interface get_all_games {
    retcode: number;
    message: string;
    data: {
        games: Game[];
    };
}