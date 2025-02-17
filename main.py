import pygame
import requests
import io

pygame.init()
WIDTH, HEIGHT = 630, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2")
font = pygame.font.Font(None, 30)
text_content = "Tere, olen Martin Mitt"
text_position = [220, 160]


def load_image_from_url(url):
    try:
        response = requests.get(url)
        image = pygame.image.load(io.BytesIO(response.content))
        return image
    except Exception as e:
        print(f"Viga pildi laadimisel: {e}")
        return None


image_data = [
    {"url": "https://www.metshein.com/wp-content/uploads/2019/03/bg_shop.jpg", "pos": [0, 0], "scale": 1.0},
    {"url": "https://www.metshein.com/wp-content/uploads/2019/03/seller.png", "pos": [70, 150], "scale": 0.3},
    {"url": "https://www.metshein.com/wp-content/uploads/2019/03/chat.png", "pos": [200, 100], "scale": 0.7},
]

images = [(load_image_from_url(data["url"]), data["pos"], data["scale"]) for data in image_data]

running = True
while running:
    screen.fill((0, 0, 0))

    for img, pos, scale in images:
        if img:
            scaled_img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            screen.blit(scaled_img, pos)

    text_surface = font.render(text_content, True, (255, 255, 255))
    screen.blit(text_surface, text_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()