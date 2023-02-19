use macroquad::prelude::*;
mod mazers;

fn window_conf() -> Conf {
    Conf {
        window_title: "Mazers".to_string(),
        window_width: 800,
        window_height: 600,
        ..Default::default()
    }
}

#[macroquad::main(window_conf)]
async fn main() {
    mazers::Game::run().await;
}
