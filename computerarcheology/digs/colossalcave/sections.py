SECTIONS = {}

with open('advent.dat', 'r') as f:
    while True:
        sec_num = int(f.readline().strip())
        if sec_num == 0:
            break
        current_section = []
        SECTIONS[sec_num] = current_section        
        while True:
            line = f.readline().strip()
            if line.startswith('-1'):
                break
            current_section.append(line)
