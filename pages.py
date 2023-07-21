from globals import *


class Pages:
    def __init__(self):
        pass

    def draw_screen(self):
        self.draw_rectangle_middle()
        self.draw_rectangle_bottom()
        self.draw_line()

    def draw_rectangle_middle(self):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300, 200, 200, 200), 1)
        screen.blit(font_default.render("1", True, (0, 0, 0)), (300, 200))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 200, 200, 200), 1)
        screen.blit(font_default.render("2", True, (0, 0, 0)), (500, 200))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300, 400, 200, 200), 1)
        screen.blit(font_default.render("3", True, (0, 0, 0)), (300, 400))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 400, 200, 200), 1)
        screen.blit(font_default.render("4", True, (0, 0, 0)), (500, 400))

    def draw_rectangle_bottom(self):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(40, 760, 200, 200),  1)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(280, 760, 200, 200), 1)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(520, 760, 200, 200), 1)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(760, 760, 200, 200), 1)

    def draw_line(self):
        pygame.draw.line(screen, (0, 0, 0), (0, 720), (1000, 720), 3)

    def page_main(self):
        screen.fill((255, 255, 255))
        screen.blit(image_background, (0, 0))

        font_page_main = pygame.font.SysFont("calibri", 80, True)
        screen.blit(font_page_main.render(
            "PUZZLE ZOO", True, "black"), (250, 630))

        pygame.draw.circle(screen, (0, 255, 0), [500, 780], 50)
        screen.blit(image_button_next, (460, 740))

    def update_page(self, number_page: float):
        pygame.display.update()
        page = number_page
        return page
