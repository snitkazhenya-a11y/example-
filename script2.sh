Bash
#!/bin/bash
echo "Яку папку ти хочеш створити?"
read folder_name
mkdir "$folder_name"
echo "Папку '$folder_name' успішно створено!"