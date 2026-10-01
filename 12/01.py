def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
        
    cleaned_text = ""
    inside_tag = False
    
    for char in html:
        if char == '<':
            inside_tag = True
            continue
        elif char == '>':
            inside_tag = False
            continue
            
        if not inside_tag:
            cleaned_text += char
            
    
    lines = cleaned_text.splitlines()
    
    non_empty_lines = []
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line: 
            non_empty_lines.append(cleaned_line)
            
    final_text = '\n'.join(non_empty_lines)
            
    
    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(final_text)

delete_html_tags('12/draft.html', '12/cleaned.txt')
print("Готово!")