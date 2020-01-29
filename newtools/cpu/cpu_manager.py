import cpu.base_cpu

_CPUS = {}


def get_cpu_by_name(name: str) -> cpu.base_cpu.CPU:

    if name in _CPUS:
        return _CPUS[name]

    # Delayed imports ... only for the processors we need

    cp = None
    if name == '6502':
        import cpu.cpu_6502
        cp = cpu.cpu_6502.CPU_6502()
    elif name == '6803':
        import cpu.cpu_6803
        cp = cpu.cpu_6803.CPU_6803()
    elif name == '6809':
        import cpu.cpu_6809
        cp = cpu.cpu_6809.CPU_6809()
    elif name == '8052':
        import cpu.cpu_8052
        cp = cpu.cpu_8052.CPU_8052()
    elif name == 'DVG':
        import cpu.cpu_DVG
        cp = cpu.cpu_DVG.CPU_DVG()
    elif name == 'Z80':
        import cpu.cpu_Z80
        cp = cpu.cpu_Z80.CPU_Z80()
    elif name == 'Z80GB':
        import cpu.cpu_Z80GB
        cp = cpu.cpu_Z80GB.CPU_Z80GB()

    if cp:
        _CPUS[name] = cp

    return cp
