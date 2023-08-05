import os
import pygame
import pygame_gui
import time

# Constants for colors
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set the dimensions of the canvas
canvas_width, canvas_height = 800, 600

# Create the canvas
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Free Draw - Red Pen")

# Create a UI manager
ui_manager = pygame_gui.UIManager((canvas_width, canvas_height))

# Create a separate surface for drawing
draw_surface = pygame.Surface((canvas_width, canvas_height), pygame.SRCALPHA)

# Variables for drawing
drawing = False
last_pos = None
brush_size = 5


def draw_on_canvas(start_pos, end_pos):
    pygame.draw.line(draw_surface, RED, start_pos, end_pos, brush_size)


def save_canvas_as_image():
    folder_path = "C:/Users/MIS/Desktop/letter det"
    timestamp = time.strftime("%Y%m%d%H%M%S")
    file_name = f"drawn_image_{timestamp}.png"
    file_path = os.path.join(folder_path, file_name)
    pygame.image.save(draw_surface, file_path)


# Add a "Save As" button
save_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (100, 30)), text="Save As", manager=ui_manager
)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if save_button.rect.collidepoint(event.pos):
                    # Save the drawn image
                    save_canvas_as_image()
                else:
                    drawing = True
                    last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = pygame.mouse.get_pos()
            draw_on_canvas(last_pos, current_pos)
            last_pos = current_pos

        ui_manager.process_events(event)

    # Draw the canvas with the drawing surface
    canvas.fill((255, 255, 255))  # Fill the canvas with white (optional)
    canvas.blit(draw_surface, (0, 0))

    # Update the UI manager and draw the "Save As" button
    ui_manager.update(1 / 60)
    ui_manager.draw_ui(canvas)

    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()
