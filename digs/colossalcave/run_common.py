import fortran_env

def run_common(line,frame):
    if frame.section_name == '*':
        # Ignore these lists in the root section
        return
    else:
        # In other sections, copy the pointers from the root
        raise NotImplementedError(f"COMMON block in section {frame.section_name} not implemented")