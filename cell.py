import pygame


class Cell:
    temp_mapping = {1: (1, 1), 2: (2, 1), 3: (3, 1), 4: (1, 2), 5: (2, 2), 6: (3, 2), 7: (1, 3), 8: (2, 3), 9: (3, 3)}
    number_color_mapping = {1: (255, 0, 0), 2: (0, 255, 0), 3: (0, 0, 255), 4: (255, 255, 0), 5: (255, 0, 255),
                            6: (0, 255, 255), 7: (180, 220, 0), 8: (180, 220, 255), 9: (0, 0, 0)}

    def __init__(self, row, col, value, width, height, permanent):
        self.row = row
        self.col = col
        self.value = value
        self.width = width
        self.height = height
        self.permanent = permanent
        self.temp_values = set()
        self.selected = False
        self.fnt_p = pygame.font.SysFont(pygame.font.get_default_font(), 40)
        self.fnt_t = pygame.font.SysFont(pygame.font.get_default_font(), 15)

    def set_value(self, value):
        if 0 <= value <= 9:
            # if we want to delete a number from this cell
            if value == 0:
                self.value = 0
            # if we want to write a new number to this cell
            else:
                self.value = value
                self.temp_values.clear()

    def set_temp_value(self, temp_val):
        # each cell can have at most 8 temp values
        if temp_val not in self.temp_values:
            if 0 < temp_val <= 9 and len(self.temp_values) < 8:
                self.temp_values.add(temp_val)
                self.value = 0
        else:
            if temp_val in self.temp_values:
                self.temp_values.remove(temp_val)

    def draw(self, window):

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if not (self.value == 0):
            text = self.fnt_p.render(str(self.value), True, self.number_color_mapping[self.value])
            window.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        elif len(self.temp_values) != 0 and self.value == 0:
            for val in self.temp_values:
                text = self.fnt_t.render(str(val), True, (128, 128, 128))
                window.blit(text, (x + self.temp_mapping[val][0] * 15, y + self.temp_mapping[val][1] * 15))

        if self.permanent:
            pygame.draw.rect(window, (0, 0, 0), (x, y, gap, gap), 3)
        if self.selected:
            pygame.draw.rect(window, (255, 0, 0), (x, y, gap, gap), 3)
