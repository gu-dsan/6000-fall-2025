library(gt)
library(glue)
library(knitr)
library(tidyverse)
library(gtExtras)
library(kableExtra)

get_schedule_as_table <- function() {  
    withr::with_dir(here::here(), {
    schedule_nested <- read_csv(here::here(file.path("data", "schedule.csv")))
    schedule_ical_file <- file.path("files", "schedule.ics")
    })
    course_number <- yaml::read_yaml(here::here("_variables.yml"))$course$number
    semester <- yaml::read_yaml(here::here("_variables.yml"))$course$semester

    num_phases <- length(unique(schedule_nested$subgroup))
    phases <- paste(unique(schedule_nested %>% select(group) %>% drop_na() %>% pull(group)), collapse=", ")

    schedule_nested[is.na(schedule_nested)] <- ""

    schedule_nested %>%
      select(group, subgroup, date, title, notes) %>%
      gt(rowname_col = "group", groupname_col = "subgroup") %>%
      gt_highlight_rows(columns = c("title"),
                        rows = str_detect(title, "NO CLASS"),
                        fill = "#80bcd8",
                        alpha = 0.8,
                        font_weight = "bold",
                        font_color = "#000000",
                        bold_target_only = FALSE,
                        target_col = c()) %>%
      cols_width(    
        starts_with("date") ~ px(100)
      ) %>%
      cols_label(
        group = "Category",
        subgroup = "Subgroup",
        date = "Date",
        title="Module",
        notes="Notes"
      ) %>%
      tab_header(title=glue("Schedule for the semester {course_number} {semester}"),
                 subtitle=glue("This course is divided into {num_phases} phases: {phases}.")) %>%
      tab_style(
          locations = cells_column_labels(columns = everything()),
          style     = list(
          #Give a thick border below
          cell_borders(sides = "bottom", weight = px(3)),
          #Make text bold
          cell_text(weight = "bold")
          )
      ) %>% 
      #Apply different style to the title
      tab_style(
          locations = cells_title(groups = "title"),
          style     = list(
          cell_text(weight = "bold", size = 24)
          )
      ) %>%
      fmt_markdown(columns = c("title", "notes"))
}
