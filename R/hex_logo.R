# install.packages("hexSticker")

library(ggplot2)
library(png)
library(grid)
library(hexSticker)

## Settings:
col_text <- "#4B77BE"
col_ribbon <- "#ABB7B7"
col_bg <- "#FFFFFF"
course <- "PPOL-5206"
withr::with_dir(here::here(), {
  print(here::here())
  logo_png <- file.path("files", "img", "logo.png")
  logo_hex_sticker = file.path("files", "img", "ppol5206-logo.png")
})

logo <- readPNG(logo_png)
logo <- rasterGrob(logo,
                   width = .75,
                   x = 0.5,
                   y = 0.5,
                   interpolate = TRUE)

gg <- ggplot() +
 annotation_custom(logo) +
  theme_void()

sticker(gg, package=course, p_size=18, s_x=1, s_y=.75, s_width=1.3, s_height=1,
            p_color=col_text, # text color
            h_fill=col_background, # color for the background fill
            h_color=col_bg, # color of the ribbon
            filename=logo_hex_sticker)


