$files = @(
    "task_2.sql",
    "task_5.sql",
    "task_6.sql",
    "task_3.sql",
    "task_4.sql"
)

foreach ($file in $files) {
    mysql -u root -p -e "SOURCE C:/Users/ADMIN/OneDrive/Desktop/ALX PROJECTS/BACK-END WEB DEVELOPMENT/Intro_to_DB/$file;"
}
